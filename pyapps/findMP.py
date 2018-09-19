'''
Created on Aug 9, 2018

@author: hal
'''
from functools import partial
import pyodbc
from threading import Thread
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

from basic_interface import BasicDBOut
from sqldata_retrieve import SqlRetrieve, SqlRetrieveThreading


def retrieve_data(short_plu, date_str):
#     connectString = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='
#     db = pyodbc.connect(connectString)
#     cursor = db.cursor()
#     if cursor.tables(table='pdlist').fetchone():
#         cursor.execute("""select mpid, shortplu, startdate, enddate 
#                         from pdlist 
#                         where 
#                             shortplu = ?
#                             and startdate <= '?' and enddate >= '?'""", short_plu, date_str, date_str)  
#     else:
#         print('Table NOT exist')
#           
#     columns = [[column[0], column[3]] for column in cursor.description]#get column name and column size   
#     result_q = cursor.fetchall()
# #     result_q.insert(0, columns)
#     
#     db.close()        
#     return columns, result_q
    pass
 
def call_retrieve(a_tv, a_plu_entry, a_de, a_tk_var, a_pb):
    try:
        result_q = pdlist_table.connect_retrieve_db()
        col_names, recs = result_q
    except Exception as e:
        db_err = e.args[1] if e.args[1:2] else e.args[0] #check args[1] exist. Return [] if args[1] NOT exist while check directly on args[1] will throw exception if it NOT exist
        i = db_err.find(':')     #exception is tuple of args strings
        if i > 0:
            db_err = db_err[:i]
            
        print(db_err)
        a_tk_var.set(db_err)
        return        
    
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
    
    a_pb.stop() 
        
    return

def thread_db_retrieve(*wg_args):
    t = Thread(target=call_retrieve, args=wg_args)
    t.start()

#Decorator for Button callback function
def gui_db_buttoncall(funct):
    pass


gui = Tk()
gui.title("Find Active MP")
gui.geometry("900x500")

basic_dbout = BasicDBOut(gui, 'Plu Short', 1)
basic_dbout.basic_setting(thread_db_retrieve)
basic_dbout()   #class obj is NOT callable. However, I implemented __call__ in it, so it is now callable

short_plu = basic_dbout.user_entry.get()
date_str = str(basic_dbout.user_date_pick.get_date())

conn_str = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='

#     sql_str = """select *
#                         from pdlist
#                         where
#                             shortplu = {}
#                             and startdate <= '{}' and enddate >= '{}'""".format(short_plu, date_str, date_str)

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
#     pdlist_table = SqlRetrieveThreading(conn_str, sql_str)  
pdlist_table.connect_retrieve_db()   
basic_dbout.msg.set('Retrieving data. Please wait...')                 


 


# basic_dbout.prg_bar.stop()  

gui.mainloop()
