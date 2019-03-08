'''
Created on Aug 30, 2018

@author: hal
'''
from sqlite3.test import dbapi
'''
Note on Class variable: a1, a2 are instants of A. without further assignment, a1.name, a2.name resolve(reference) to A.name.
With further assignment as below, a1.name, a2.name turn into data attributes. Data attributes like local variables, they spring into existence when they are first assigned to.
I.e, a1.name, a2.name != A.name (a1.name, a2.name are newly created instance variable of instance a1 and a2 as such they were declare with 'self' in __init__)
class A:
    name = "Dog"

a1 = A()
a2 = A()

# These both change the value only for an instance
a1.name = "Cat"
a2.name += " is an animal"
print(a1.name, a2.name) ==> 'Cat Dog is an animal'
del a1.name
del a2.name
print(a1.name, a2.name) ==> 'Dog Dog' #now they resolved back to A.name (Class variable)
'''

from functools import partial
from threading import Thread
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

class BasicDBOut:
    '''
    basic output for database retrieve: a TreeView, a Button, and a Message screen
    '''
    
    @staticmethod
    def thread_db_retrieve(inst, *wg_args): #inst is inst of self, got passed in command='...'
        inst.msg.set('Retrieving data. Please wait...')  
        t = Thread(target=inst.button_callback, args=wg_args)
        t.start()
    
    def __init__(self, gui, ue_label, with_button=0):       
        self.parent_gui = gui
        self.db_access = None
        
        self.user_entry_frame = Frame(self.parent_gui, padx = 2, pady = 5)
        self.data_out_frame = Frame(self.parent_gui, padx = 2, pady = 5)
        self.msg_frame = Frame(self.parent_gui, padx = 2, pady = 5)
        self.s = ttk.Style()
        self.s.configure('self.Treeview', rowheight=15)     
        self.user_entry_label = Label(self.user_entry_frame, text=ue_label) 
        self.s_y = Scrollbar(self.data_out_frame)
        self.s_x = Scrollbar(self.data_out_frame, orient=HORIZONTAL)
        self.tv = ttk.Treeview(self.data_out_frame, style='self.Treeview', yscrollcommand=self.s_y.set, xscrollcommand = self.s_x.set)
        self.s_y.config(command=self.tv.yview)
        self.s_x.config(command=self.tv.xview)
        self.msg = StringVar() #showing completion or error message
        self.msg_bar = Label(self.msg_frame ,textvariable=self.msg, bg = 'white', fg = 'blue')
        self.prg_bar = Progressbar(self.msg_frame, mode='indeterminate')
        self.user_entry = Entry(self.user_entry_frame)
        self.user_date_pick = DateEntry(self.user_entry_frame)
        if with_button:            
            #need use lambda to pass self as arg. thread_db_retrieve(...) is staticmethod, so self.thread_db_retrieve doesn't bind into bound method obj
            self.retrieve_button = ttk.Button(self.user_entry_frame, text="Retrieve", command = lambda: self.thread_db_retrieve(self))
        
    def basic_setting(self, *args):
        self.user_entry_frame.pack(anchor = NW)
        self.data_out_frame.pack(anchor = NW, fill = BOTH, expand = 1)
        self.msg_frame.pack(anchor = NW, fill = BOTH)
        self.user_entry_label.pack(side = LEFT)
        self.user_entry.pack(side = LEFT)
        self.user_entry.insert(0, "959714")
        self.s_y.pack(side=RIGHT, fill=Y)
        self.tv.pack(anchor = NW, fill = BOTH, expand = 1)
        self.s_x.pack(fill=X)
        self.prg_bar.pack(fill=X)
        self.prg_bar.start(500)
        self.prg_bar.step()        
        self.msg_bar.pack(fill=X, padx = 15, pady = 2)
        self.user_date_pick.pack(side = LEFT, padx = 5)
        if hasattr(self, 'retrieve_button'):
            self.retrieve_button.pack(side = LEFT, padx = 5)
#             self.retrieve_button.configure(command = partial(button_func, *button_func_args))
        
    def __call__(self): #holder to implement this module to callable object later
        print(repr(self), 'is now callable and got called')
        
    def __repr__(self):
        return str(BasicDBOut) + '(Obj, NOT class):'
    
    def retrv_db(self):
        try:            
            db_return = self.db_access.connect_retrieve_db()
        except Exception as e:
#             db_err = e.args[1] if e.args[1:2] else e.args[0] #check args[1] exist. Return [] if args[1] NOT exist while check directly on args[1] will throw exception if it NOT exist
            db_err = e.args[1:2] or e.args[0] #ATTENTION!!: A = ((X and Y) or Z). if Y evaluates to 'False', CAN'T use it replace if...else...
                                              #semantic: evaluate left to right, on False return the latest item
            i = db_err.find(':')     #exception is tuple of args strings
            if i > 0:
                db_err = db_err[:i]
                
            print(db_err)
            self.msg.set(db_err)
            raise #re-raise previous exception

        return db_return
    
    def button_callback(self):       
        try:
            col_names, recs = self.retrv_db()
        except Exception as ee:
            print(ee)
            return #already handle in retrv_db
        
        self.tv.delete(*self.tv.get_children())   #return list of children of root and splatted(unpack list)
        self.tv['columns'] = [col_name for col_name in col_names]
        self.tv['show'] = 'headings'
        for col_name in col_names:
            self.tv.heading(col_name, text=col_name)
            self.tv.column(col_name, anchor='center', stretch = 0)
        if recs: 
            for rec in recs:
                self.tv.insert("", 0, text = str(rec[0]), value=list(rec))   #value accepts list, but rec is tuple, so need convert to list
            self.msg.set('Plu: {}, Date: {}\n Recs: {}'.format(self.user_entry, self.user_date_pick, len(recs)))
        else:
            self.msg.set('Plu: {}, Date: {}\n No Recs Found'.format(self.user_entry, self.user_date_pick))
        
        self.prg_bar.stop() 
    
#===============================================================================
# if __name__ == '__main__':
#     gui = Tk()
#     gui.title("Find Active MP")
#     gui.geometry("900x500")
#     
#     basic_dbout = BasicDBOut(gui, 1)
#     
#     plu_label = Label(basic_dbout.user_entry_frame ,text="Short Plu").pack(side = LEFT)
#     
#     basic_dbout.basic_setting()
#     
#     gui.mainloop()        
#===============================================================================