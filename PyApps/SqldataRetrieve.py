'''
Created on Aug 24, 2018

@author: hal
'''

'''argument vs parameter'''
'''You define parameters(on function), you make arguments(calling function)'''

from threading import Thread
import pyodbc
from MyUtils import printnl


class SqlRetrieve:
    '''
    Connect to database and retrieve corresponding sql 
    
    Attributes:
        sql_str: sql string to retrieve
        conn: Pyodbc connection to connect to db
        cur: db cursor
    '''
    
    _conn_str = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='

    def __init__(self, a_sql_str):
        '''
        Constructor
        '''
        self.sql_str = a_sql_str
        self.conn = pyodbc.connect(self._conn_str)
        self.cur = self.conn.cursor()
        self.col = None
        
    def connect_retrieve_db(self, a_sql_str = None):
        #         if cursor.tables(table='pdlist').fetchone():
        if a_sql_str is not None:
            self.sql_str = a_sql_str
            
        try:            
            self.cur.execute(self.sql_str)
        except Exception as e:
            print(e)
            return 
              
        self.col = [column[0] for column in self.cur.description]#get column name and column size   
        result_q = self.cur.fetchall()
#         self.conn.close()    
            
        return result_q    #cursor.description still exist after return. feature of pyodbc
#         return self.cur

#     def dec_dbaccess(self, func):




#===============================================================================
####Calling Thread() function to run thread through function, NOT using class implementation
# class threading.Thread(group=None,
#                        target=None,
#                        name=None,
#                        args=(),
#                        kwargs={})
#
# group: This is the value of group that should be None; this is reserved for future implementations
# target: This is the function that is to be executed when you start a thread activity
# name: This is the name of the thread; by default, a unique name of the form Thread-N is assigned to it
# args: This is the tuple of arguments that are to be passed to a target
# kwargs: This is the dictionary of keyword arguments that are to be used for the target function    
#===============================================================================
class SqlRetrieveThreading(SqlRetrieve, Thread):
    #If inherit one class and no additional code in init of this subclass, no need to overwrite init
    #subclass will call parent init by itself.
    #If inherit multiple classes, need explicitly call parents init or code super.__init__() in each class 
    #to follow Method Resolution Order(MRO)
    #
    def __init__(self, *args):
#         super().__init__(*args)    #if use this, need to code it in parent also(in this case: SqlRetrieve class)
#         SqlRetrieve.__init__(*args)
#         Thread.__init__(self)
        pass
            
        
#     def run(self):
#         return self.connect_retrieve_db(a_sql_str)



if __name__ == '__main__':
    sql_str = '''
        select * from invbillinfo_mp
        where
            invoicedate >= '2019-02-01'
            and reason = 56
            and recordtype in (7, 207)
            and plu = 497837
        '''
    sqlR = SqlRetrieve(sql_str)
    result = sqlR.connect_retrieve_db()
    printnl(sqlR.col, *result)