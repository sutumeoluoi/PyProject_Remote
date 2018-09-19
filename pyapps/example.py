'''
Created on Aug 2, 2018

@author: hal
'''

#import sys
# import pyodbc
#from pyodbc import Cursor

#===============================================================================
# from sqlalchemy import create_engine
# import urllib
# from zipfile import _CD64_DIRECTORY_RECSIZE
#===============================================================================
#===============================================================================
# conn_str = (
#     r'DRIVER={Pervasive ODBC Client Interface};'
#     r'SERVERNAME=ISD101;'
#     r'DBQ=TEMPDB;'
#     r'UID=;'
#     r'PWD='
# )
# quoted_conn_str = urllib.parse.quote_plus(conn_str)
# engine = create_engine('sqlalchemy-pervasive+pyodbc:///?odbc_connect={}'.format(quoted_conn_str))
# cnxn = engine.connect()
# rows = cnxn.execute("SELECT * FROM associat WHERE emplnum between  98 and 100").fetchall()
# print(rows)
#===============================================================================

#===============================================================================
# connection_string = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=ISD101;DBQ=TEMPDB;UID=;PWD='
# connection_string = urllib.parse.quote_plus(connection_string) 
# connection_string = "sqlalchemy-pervasive+pyodbc:///?odbc_connect=%s" % connection_string
# engine = create_engine(connection_string)
# cnxn = engine.connect()
# rows = cnxn.execute("SELECT * FROM associat WHERE emplnum between  98 and 100").fetchall()
# print(rows)
#===============================================================================

# How to fetch recs from database
#===============================================================================
# cursor.execute("SELECT id, name FROM `table`")
# for i in xrange(cursor.rowcount):
#     id, name = cursor.fetchone()
#     print id, name
# 
# 
# cursor.execute("SELECT id, name FROM `table`")
# result = cursor.fetchmany()
# while result:
#     for id, name in result:
#         print id, name
#     result = cursor.fetchmany()
# 
# 
# cursor.execute("SELECT id, name FROM `table`")
# for id, name in cursor.fetchall():
#     print id, name
#===============================================================================

#===============================================================================
# ### Specifying the ODBC driver, server name, database, etc. directly
# connectString = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=ISD101;DBQ=TEMPDB;UID=;PWD='
# # connectString = 'DRIVER={Pervasive ODBC Client Interface};SERVERNAME=MASTER101;DBQ=MMV8;UID=;PWD='
# ### Using a DSN, but providing a password as well
# #connectString = 'DSN=ISD101TEMPDB;UID=;PWD='
# db = pyodbc.connect(connectString)
# 
# #var = input("Please enter something: ")
# #print("You entered " + str(var))
# 
# cursor = db.cursor()
# # if cursor.tables(table='pdlist').fetchone():
# cursor.execute("SELECT * FROM associat WHERE emplnum between  98 and 100")
# #     cursor.execute("""select mpid, shortplu, startdate, enddate 
# #                     from pdlist 
# #                     where 
# #                         shortplu = 959714 
# #                         and startdate <= '2018-8-4'
# #                         and enddate >= '2018-8-4'""")    
# # else:
# #     print('Table NOT exist')
#     
# # desc = cursor.description
# # print(desc)
# 
# # columns = [[column[0], column[3]] for column in cursor.description]
# # print(columns)
# print(cursor.fetchall())
# # for i in range(len(desc)):
# #     print(desc[i][0].rjust(12), end=' ') 
# # print('', end='\n')      
# 
# # #for row in cursor.fetchall():
# # for row in cursor:
# #     for column in row:
# #         print (str(column).rjust(10), end='\t') 
# #     print('',end='\n')
# 
# # cursor_1 = db.cursor()
# # for row in cursor_1.columns(table='pdlist'):
# #     #if row.column_name not in ['Expansion', 'Approved']:
# #        print (row[0], end='\t')
# # print('', end='\n')
# 
# # table_details = cursor.columns(table='pdlist')
# # for row in cursor.columns(table='pdlist'):
# #     print(row)
#    
# #for row in cursor_1.tables(): 
# #    print (row.table_name)       
#           
# 
# db.close()
# 
# '''
# row in cursor.execute("select user_id, user_name from users"): print row.user_id, row.user_name
# 
# row = cursor.execute("select * from tmp").fetchone() 
# rows = cursor.execute("select * from tmp").fetchall()
# 
# count = cursor.execute("update users set last_logon=? where user_id=?", now, user_id).rowcount 
# count = cursor.execute("delete from users where user_id=1").rowcount 
# '''
#===============================================================================

#===============================================================================
# n = {'barry': [0, 0], 'bob': [0, 0], 'james': [0, 0]}
# l = [{'timestamp': '20180903-223223', 'name': 'barry', 'change': '0.2', 'changepc': '1.48'}, 
#      {'timestamp': '20180903-223223', 'name': 'bob', 'change': '-0.05', 'changepc': '-1.02'}]
# 
# for item in l:
#     if item['name'] in n:
#         change = float(item['change'])
#         if change > 0:
#             n[item['name']][0] += 1
# #             print("name = {} increase = {}".format(item['name'], change))
#         elif change < 0:
#             n[item['name']][1] += 1
#     
# print(n)
#===============================================================================

#===============================================================================
# l = [{'timestamp': '20180903-223223', 'name': 'barry', 'change': '0.2', 'changepc': '1.48'}, 
#      {'timestamp': '20180903-223223', 'name': 'bob', 'change': '-0.05', 'changepc': '-1.02'}] 
#    
# with open('counterfile.txt', 'r') as f:
#     chgs_dict = {name: list(map(int, value)) for name, *value in [n.split() for n in f]}
# print(chgs_dict)
#             
# # for item in l:
# #     if item['name'] in dict_names:
# #         change = float(item['change'])
# #         if change > 0:
# #             dict_names[item['name']][0] += 1
# #         elif change < 0:
# #             dict_names[item['name']][1] += 1                 
# # print(dict_names)
# 
# for n in l:
#     if n['name'] in chgs_dict:
#         chg = float(n['change'])
#         if chg > 0.00:
#             #print(str(n['name']) + " changed by " + str(n['change']))
#             chgs_dict[n['name']][0] += 1
#         elif chg < 0.00:
#             #print(str(n['name']) + " changed by " + str(n['change']))
#             chgs_dict[n['name']][1] += 1
#         else:
#             print(str(n['name']) + " no change")
#     #         pass
# print(chgs_dict)
#   
# for k, val in chgs_dict.items():
# #     print(k, ': ', str(v[0]), str(v[1]))    
#     if all(v == 0 for v in val):
#         print(k, 'has no change')
#     else:
#         print(k + ' changed by')
# #     print(k if all(v == 0 for v in val) else None)
#===============================================================================
   
# scores = [100,  100, 50, 40, 40, 20, 10]
# alice = [5, 25, 50, 120]
#   
# prev_item_rk = 0
# al_rks = [0]*len(alice)
# rk = 0
# n = len(alice)-1
# for item_rk in scores:        
#     if item_rk != prev_item_rk:
#         rk += 1
#         for i in range(n, -1, -1):                
#             if alice[i] >= item_rk:
#                 al_rks[i] = rk 
#                 n -= 1
#             else:
#                 break   #anything after alice[i] must < item_rk since alice sorted
#         prev_item_rk = item_rk                
#   
# for i, al_rk in enumerate(al_rks):
#     if al_rk == 0:
#         al_rks[i] = rk + 1
#     else:
#         break
#    
# print(al_rks)        



#===============================================================================
# s = 'candleg'
# s = list(s.upper())
# for i in range(1, len(s), 2):
#     s[i], s[i-1] = s[i-1], s[i]
# print(''.join(s))
#===============================================================================

#===============================================================================
# # 'candle' becomes 'ACDNEL'
# word = 'candleg'
# new_word = ''.join(word[i:(i+2)][::-1] for i in range(0, len(word), 2)).upper() #join accept iterables(list, tuple, generator, iterator...)
# print(new_word)
#===============================================================================

#===============================================================================
#===============================================================================
# with open("in-out.txt", "r") as f:
#     read_list = [line.rstrip('\n') + " is an excellent webcomic\n" for line in f]
# print(read_list) 
#  
# with open("in-out.txt", "w") as f:
#     f.writelines(read_list)
#===============================================================================
#===============================================================================

#===============================================================================
# #####populate 2d list from user input
# n= 5
# a = []
# for a_i in range(n): 
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')] 
#     a.append(a_t)
#===============================================================================

#===============================================================================
# l = [1 if x >0 else -1 for x in arr if x != 0]
# print("%.6f" % float(l.count(1)/n))
# print("%.6f" % float(l.count(-1)/n))
# print("%.6f" % float(abs(len(l)-n) /n))
#===============================================================================

# arr = [[11, 2, 4],
#        [4, 5, 6],
#        [10, 8, -12]
#        ]
# diff = [itm[i] - itm[-(i+1)] for i, itm in enumerate(arr)]
# print(diff)        

#!/bin/python

#===============================================================================
# ar = [-4,  3,  -9,  0,  4,  1]
# print('{:6f}\n{:6f}'.format(sum([1 for item in ar if item > 0])/len(ar), sum([1 for item in ar if item < 0])/len(ar)))
#===============================================================================

#===============================================================================
# import sys
# import inspect
# print(sys.getrecursionlimit())
# print('stack len b4: {}'.format(len(inspect.stack())))
# # sys.setrecursionlimit(100)
# def check_recur_depth(count):
#     if count == 0:
#         print('stack len at deepest recur: {}'.format(len(inspect.stack())))
#         return
#          
#     check_recur_depth(count - 1)    
#     print(count)
# #     print(len(inspect.stack()))    
# try:    
#     check_recur_depth(980)
# except Exception as e:
#     print('stack len with e: {}'.format(len(inspect.stack())))
#      
# print('stack len without e: {}'.format(len(inspect.stack())))
#===============================================================================

# from itertools import chain
# import timeit
# 
# start_time = timeit.default_timer()   
# # n, k = 28, 2
# n, k = 199112, 2
# output = []
# # output = ()
# if not k:
#     output = range(1, n+1)
# elif n % (2*k):
#     output = iter((-1,))
# else:
#     t = zip(range(1, n+1, k), range(k+1, n+2, k))    
#     for i in range(n//(2*k)):
# #         odd, even = next(t), next(t)
# #         output += list(range(*even)) + list(range(*odd))
# #         output = chain.from_iterable([output, range(*even), range(*odd)])
#         output += list(chain(range(*b), range(*a)) for a, b in zip(t, t))
# #         output += list(chain.from_iterable([range(*b), range(*a)]) for a, b in zip(t, t))
#    
# output = list(chain.from_iterable(output)) 
# print(output)   
# print(timeit.default_timer() - start_time)     

#===============================================================================
# print(range(5))
# print([range(5)])
# print(*[range(5)])    
#===============================================================================

#===============================================================================
# import itertools
# line = '-' * 37
# print(line)
# print("|    №   | isdigit | isdecimal | chr")
# print(line)
# for number in itertools.chain(range(1000), range(4969, 4978), range(8304, 11000)):
#     char = chr(number)
#     if (char.isdigit() or char.isdecimal()):
#         print('| {0:>6} | {1:^7} | {2:^9} | {3:3} '.format(
#             number,
#             '+' if char.isdigit() else '-',
#             '+' if char.isdecimal() else '-',
#             char
#         )
#     )
#===============================================================================

num = 567
num_weight = sum(map(int, list(str(num))))
print(num_weight)
