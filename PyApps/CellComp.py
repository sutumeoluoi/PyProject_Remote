'''
Created on Aug 26, 2018

@author: hal
'''
import _functools
from unittest.test.testmock.testpatch import function
from ntsecuritycon import DS_BEHAVIOR_WIN2000
'''
Created on Aug 9, 2018

@author: hal
'''
from functools import partial
import pyodbc
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

from sqldata_retrieve import SqlRetrieve
 
def call_retrieve(a_tv, a_plu_entry, a_de, a_tk_var, a_pb):
    short_plu = a_plu_entry.get()
    date_str = str(a_de.get_date())
    
    conn_str = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='
    sql_str = """select *
                        from pdlist 
                        where
                            shortplu = {}
                            and startdate <= '{}' and enddate >= '{}'""".format(short_plu, date_str, date_str)

#     sql_str = """
#                 select monthstartdate, vendor, sum(vendorrebateamount)
#                         from accrec_ca
#                         where monthstartdate = '2018-8-01' and division > 0 
#                         group by monthstartdate, vendor """

#     sql_str =   """
#                 select itm.vennumprim, sum(invbillinfo_ca.qty * invbillinfo_ca.vendorrebate)
#                 from invbillinfo_ca, itm where
#                     invbillinfo_ca.plu = itm.itmplu
#                     and (invbillinfo_ca.recordtype = 3 or invbillinfo_ca.recordtype = 5)
#                     and invbillinfo_ca.invoicedate between '2018-8-01' and '2018-8-30'
#                     group by itm.vennumprim
#                 """
                                
    pdlist_table = SqlRetrieve(conn_str, sql_str)                            
    try:
        result_q = pdlist_table.connect_retrieve_db()
        col_names, recs = result_q
#         pdl_cur = pdlist_table.connect_retrieve_db()
#         col_names = [column[0] for column in pdlist_table.cur.description]#get column name and column size   
#         recs = pdl_cur.fetchall()
    except Exception as e:
        print(e)
        a_tk_var.set(e)
        return
        
    
    a_pb.stop()    
#     print(type(result_q))
    a_tv.delete(*a_tv.get_children())   #return list of children of root and splatted(unpack list)
    a_tv['columns'] = [col_name for col_name in col_names]
    a_tv['show'] = 'headings'
    for col_name in col_names:
        a_tv.heading(col_name, text=col_name)
        a_tv.column(col_name, anchor='center', stretch = 0)
    if recs: 
        for rec in recs:
            a_tv.insert("", 0, text = str(rec[0]), value=list(rec))   #value accepts list, but rec is tuple, so need convert to list
        a_tk_var.set('Plu: {}, Date: {}\n Recs: {}'.format(short_plu, date_str, len(recs)))
    else:
        a_tk_var.set('Plu: {}, Date: {}\n No Recs Found'.format(short_plu, date_str))

    return

def call_retrieve_new(a_tv, a_plu_entry, a_de, a_tk_var, a_pb):
    short_plu = a_plu_entry.get()
    date_str = str(a_de.get_date())
    
    conn_str = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='
  
#     sql_str = """
#                 select monthstartdate, vendor, sum(vendorrebateamount)
#                         from accrec_ca
#                         where monthstartdate = '2018-8-01' and division > 0 
#                         group by monthstartdate, vendor """

    sql_str =   """
                select itm.vennumprim, sum(invbillinfo_ca.qty * invbillinfo_ca.vendorrebate)
                from invbillinfo_ca, itm where
                    invbillinfo_ca.plu = itm.itmplu
                    and (invbillinfo_ca.recordtype = 3 or invbillinfo_ca.recordtype = 5)
                    and invbillinfo_ca.invoicedate between '2018-8-01' and '2018-8-30'
                    group by itm.vennumprim
                """
                                
    pdlist_table = SqlRetrieve(conn_str, sql_str)                            
    try:
        result_q = pdlist_table.connect_retrieve_db()
        col_names, recs = result_q
    except Exception as e:
        print(e)
        a_tk_var.set(e)
        return
        
    
    a_pb.stop()    
#     print(type(result_q))
    a_tv.delete(*a_tv.get_children())   #return list of children of root and splatted(unpack list)
    a_tv['columns'] = [col_name for col_name in col_names]
    a_tv['show'] = 'headings'
    for col_name in col_names:
        a_tv.heading(col_name, text=col_name)
        a_tv.column(col_name, anchor='center', stretch = 0)
    if recs: 
        for rec in recs:
            a_tv.insert("", 0, text = str(rec[0]), value=list(rec))   #value accepts list, but rec is tuple, so need convert to list
        a_tk_var.set('Plu: {}, Date: {}\n Recs: {}'.format(short_plu, date_str, len(recs)))
    else:
        a_tk_var.set('Plu: {}, Date: {}\n No Recs Found'.format(short_plu, date_str))

    return


gui = Tk()
gui.title("Find Active MP")
gui.geometry("900x500")
user_entry_frame = Frame(gui, padx = 2, pady = 5)
data_out_frame = Frame(gui, padx=2, bd = 5)
msg_frame =  Frame(gui, padx=2, bd = 5)

#define custom style for the output of data. avoid use global 'Treeview'
s = ttk.Style()
s.configure('Dataout.Treeview', rowheight=20) 

a = Label(user_entry_frame ,text="Short Plu").pack(side = LEFT)
plu_entry = Entry(user_entry_frame)
# plu_entry.delete(0, END)
plu_entry.insert(0, "959714")
plu_entry.focus_set()
s_y = Scrollbar(data_out_frame)
s_x = Scrollbar(data_out_frame, orient=HORIZONTAL)
tv = ttk.Treeview(data_out_frame, style='Dataout.Treeview', yscrollcommand=s_y.set, xscrollcommand = s_x.set)
s_y.config(command=tv.yview)
s_x.config(command=tv.xview)
tk_var = StringVar() #tk_var is Tkinter variable
msg = Label(msg_frame ,textvariable=tk_var, bg = 'white', fg = 'blue')
pb = Progressbar(msg_frame, mode='determinate')
de = DateEntry(user_entry_frame)


user_entry_frame.pack(anchor = NW)
data_out_frame.pack(anchor = NW, fill = BOTH, expand = 1)
msg_frame.pack(anchor = NW, fill = BOTH)
plu_entry.pack(side = LEFT)
s_y.pack(side=RIGHT, fill=Y)
tv.pack(anchor = NW, fill = BOTH, expand = 1)
s_x.pack(fill=X)
pb.pack(fill=X)
msg.pack(fill=X, padx = 15, pady = 2)
de.pack(side = LEFT, padx = 5)


#passing function with argument to command trigger it right away. using partial to delay it until click
#or using lamda: call_retrieve(tv)
c = ttk.Button(user_entry_frame, text="Retrieve", command = partial(call_retrieve, tv, plu_entry, de, tk_var, pb)).pack(side = LEFT, padx = 5)
c = ttk.Button(user_entry_frame, text="Retrieve new", command = partial(call_retrieve_new, tv, plu_entry, de, tk_var, pb)).pack(side = LEFT, padx = 5)

pb.start(500)
pb.step()

gui.mainloop()


def property_(_func):
    you passing a.getter()
    define an inner wrapper function
    inside wrapper call a.getter() and adding more behavior
    finally_ return_ wrapper