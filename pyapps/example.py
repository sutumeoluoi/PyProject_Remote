'''
Created on Aug 2, 2018

@author: hal
'''
from itertools import cycle, chain
# server1 = ['a','b','c']
# server2 = ['d','e','f']
# server3 = ['g','h','i']
# server_names = chain.from_iterable(zip(server1, server2, server3)) 
# print(list(server_names))

#===============================================================================
# ######## Remove 0 in sub-list
# L = [[5, 0, 6], [7, 22], [0, 4, 2], [9, 0, 45, 17]]
# # L = [list(filter(lambda x: x != 0,item)) for item in L]
# # L = [list(filter(None,item)) for item in L] #None defaulted to use identity funct where false item return false. in this case 0 is false
# # L = list(map(lambda y: list(filter(lambda x: x != 0, y)) , L))
# L = [[subitem for subitem in item if subitem] for item in L]    #using nested conditional list comprehension taking advantage of 0 is false
# print(L)
#===============================================================================

# ****** SINGLETON Design Pattern
# Standard singleton design pattern, for most languages, to ensure that only one instance of 
# the class is ever created. An implementation of the singleton pattern must:
# _ ensure that only one instance of the singleton class ever exists; and
# _ provide global access to that instance.
# ***
# The constructor says:
# If there is no instance recorded, 
#    create an instance and record it
# return the recorded instance
# ***
# Using base class method
# class Singleton:
#     instance = None
#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
# 
# singleton_obj1 = Singleton()
# singleton_obj2 = Singleton()
# 
# print(singleton_obj1)
# print(singleton_obj2)
# >>> <__main__.Singleton object at 0x10dbc0f60>
# >>> <__main__.Singleton object at 0x10dbc0f60>
# 
# Using metaclass method
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
# 
# #Python2
# class MyClass(BaseClass):
#     __metaclass__ = Singleton
# 
# #Python3
# class MyClass(BaseClass, metaclass=Singleton):
#     pass
# 
# Other methods: using class decorator(define function to decorate class, at the end class turn into function
# *******************


#===============================================================================
# from collections import Counter, defaultdict
# def count_arr(arr):
#     for i, next_index in enumerate(arr):
#         if next_index > 0:
#             arr[i] = 0
#             while True:
#                 next_item = arr[next_index-1]
#                 if next_item < 0:
#                     arr[next_index-1] -= 1
#                     break
#                 elif next_item > 0:                     
#                     arr[next_index-1] = -1
#                     next_index = next_item
#                 else:
#                     arr[next_index-1] = -1
#                     break
#                 
#     return dict((i, abs(v)) for i, v in enumerate(arr, 1))
#                    
# a = [3, 4, 3, 1, 2, 1, 5, 5, 5,8]
# # ct = Counter(a)
# ct = defaultdict(int)
# for item in a:
#     ct[item] += 1
# print(sorted(ct, key=reversed))
# arr = count_arr(a)
# print(arr)
#===============================================================================


#===============================================================================
# ******Create/copy list of mutable object******
# **remember that repetition, concatenation, and slicing copy only the top level of their operand objects
# **L1, L2, X,board,... is reference to list object [2, 3, 4], [4, 5, 6],... Thus, any repetition, concatenation
# **of them just clone them(clone reference), NOT clone the object. It will create multiple copies of the same
# **object.
# L1 = [2, 3, 4]
# L2 = L1[:] # Make a copy of L1 (or list(L1), copy.copy(L1), etc.). Note: copy.copy() only works on sequences
# L2 = list(L1)
# L2 = copy.copy(L1)
# L2 = [L1]*3
# L = [1, 2, 3]
# M = ['X', L[:], 'Y'] # Embed a copy of L (or list(L), or L.copy())
# L = [4, 5, 6]
# X = L * 4 # Like [4, 5, 6] + [4, 5, 6] + ...
# Y = [L] * 4 # [L] + [L] + ... = [L, L,...]. Change L[1] change every sublist in Y
# Y = [list(L)] * 4 # Embed a (shared) copy of L. Avoid trap above, but encounter another below
# Same as Y = [L for _ in range(4)] or Y = []; for _ in range(4): Y.append(L)
# However, Y = [[4, 5, 6] for _ in range(4)] or Y = [list(L) for i in range(4)] fixed this trap
# print(Y)
# Y[0][1] = 99 # All four copies are still the same
# # Y => [[4, 99, 6], [4, 99, 6], [4, 99, 6], [4, 99, 6]]
# print(Y)
#  
#   
# board = []
# row = [0,0,0,0,0,0,0,0]
# for i in range(8):
#     board.append(row)
#     print(id(row))
# #     board.append([0,0,0,0,0,0,0,0])    #This works. Avoid the trap
# # board = [[0,0,0,0,0,0,0,0] for _ in range(8)] #This works. Avoid the trap
# def drawboard():
#     for i in board:
#         print(id(i))
# # board[0][0] = "K"
# # board[1].append("j")
# print(board)
# drawboard()
#===============================================================================

#===============================================================================
# # ******CLOSURE******
# # **A closure is a function remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope
# # **A function object remembers values in enclosing scopes regardless of whether those scopes are still present in memory
# # **A functions that refer to variables from the scope in which they were defined
# # **A function with an extended scope that encompasses nonglobal variables referenced in the body of the function 
# # but not defined there. It does not matter whether the function is anonymous or not; what matters is that it can access nonglobal
# # variables that are defined outside of its body. closures only matter when you have nested functions.
# # **A nested function that accesses values from outer local variables is also known as a closure
# funcs = []
# for i in range(4):
#     def f():
#         print(i)
#     funcs.append(f)# 
# for f in funcs:
#     f()
# # OR
# flist = []
# for i in range(3):
#     def func(x): return x * i
#     flist.append(func)
# for f in flist:
#     print(f(2))
# # There is no closure involved in above 2 codes. The functions just searches in the global scope for i. 
# # Check f.func_closure (Python 2) or f.__closure__ (Python 3) to see value = None
# # Python (apparently) just doesn't bother capturing the enclosing scope because it doesn't need to. 
# # Global scopes never go away. It doesn't capture enclosing scope(which is global), so it truly no closure
# flist = []
# def outer():
#     for i in range(3):
#         def inner(x): return x * i
#         print(inner.__closure__)
#         flist.append(inner)
# outer()
# for f in flist:
#     print(f.__closure__)
#     print(f(2))
# #Closure on i in inner() function. But, it's late-binding, so it returns 4 4 4
#===============================================================================

#===============================================================================
# a = [1, 2, 7, 9, 6]
# b = [3, 4]
# a.append(14) #add 14 to the same list
# a.extend(b)  #add b list to the same a list
# a = a + b    #create a new list joining old a and b
# a += b       #add b list to the same list. So, augmented assignment(iadd) is same ass extend()
#===============================================================================

#===============================================================================
# class Spam:
#     numInstances = 0
#     
#     def __init__(self):
#         Spam.numInstances = Spam.numInstances + 1
#         self.counter = 99
#     
#     def printNumInstances():
#         print("Number of instances created: %s" % Spam.numInstances)
#     
#     def printUnbound(self):
#         print('unbound {}', self.counter)
#         
# class Selfless:
#     def __init__(self, data):
#         self.data = data
#         
#     def selfless(arg1, arg2): # A simple function in 3.X
#         return arg1 + arg2
#     
#     def normal(self, arg1, arg2): # Instance expected when called
#         return self.data + arg1 + arg2
#===============================================================================

###### lambda TRAP!!!
## Expecting output: [2, 3, 4, 5, 6 ,7]; BUT print-out: [7, 7, 7, 7, 7, 7].
## I.e, expecting lambda closure to hold each x after each iteration, assume x going out of scope after each iteration
## Reason: each iteration creates an <function <listcomp>.<lambda> at 0x000000000222EBF8> object binding var 'x' to it. 
##         For loop never create new scope. 'x' belongs to enclosing scope of lambda(the scope where for loop belongs to),
##         so there is no closure in lambda. Closure only happens when var of local scope got encased into function object after that scope goes out
##         The function lambda objects got created with ref of 'x' of outer scope, so when outer scope call lambda obj, latest values of 'x'
##         got passed to lambda obj creates [7, 7, 7, 7, 7, 7].
## Note: for loop leak 'x' after loop finish while list comprehension doesn't. Thus, change x value after loop will change return of lambda.
##        However, changing x value after list comprehension, NOT change return value of lambda
##        Python 3, list comprehension creates own scope
## Ref: https://stackoverflow.com/questions/2295290/what-do-lambda-function-closures-capture/23557126
##        http://math.andrej.com/2009/04/09/pythons-lambda-is-broken/
##        https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
##        https://stackoverflow.com/questions/13905741/accessing-class-variables-from-a-list-comprehension-in-the-class-definition

# lds = []
# for x in range(6):
#     lds.append(lambda: x + 2)
# x = 10
# print([ld() for ld in lds])

### assign x = 0 after list comprehension NOT change return value of lambda. Lambda got closure on x with the lastes value = 5 and 
### calculate to return 7 on every lambda object
### 
# lds = [lambda: x + 2 for x in range(6)]
# x = 10
# print([ld() for ld in lds])
# print(lds[0]())
# print(lds)

#===============================================================================
# ## list comprehension leak 'x' into outside scope in python 2. However, Python 3 fixed it.
# ## Thus, python 2 will print '6' and python 3 will error "name 'x' is not defined"
# ## Ref: https://stackoverflow.com/questions/4198906/python-list-comprehension-rebind-names-even-after-scope-of-comprehension-is-thi
# lds = [lambda: x + 2 for x in range(6)]
# print(x)
#===============================================================================

#===============================================================================
# counter = 0  
# def count_misskey():
#     global count
#     counter += 1
#     any_key = 0
#     def count_any():
#         nonlocal any_key
#         any_key += 1
# #In main so def needs global to it to call. 
# #In def and nested def calls it, nested def need nonlocal NOT global to call it
#===============================================================================
    
#===============================================================================
# ATTENTION!!!: A = ((X and Y) or Z). Always try to evaluate to True and return the latest item when it stop
# Semantic: evaluate left to right 
#     1. On X true, evaluate Y; on Y true stop evaluation since next is 'or'. So return Y.  
#     2. On X false, not going to Y, jump to evaluation Z. Either Z True or False, always return Z bcauz Z is the last item
#     3. On X true, evaluate Y; on Y false, evaluate Z and return Z since Z is the last item. (CAN'T use replace an if else)
# Note: 1 and 2 can use to replace ternary Y if X else Z. 3 can't use since it return Z on X true and Y false.
#     I.e, only use it to replace Y if X else Z when you are sure Y always TRUE!!!!
#===============================================================================

#===============================================================================
# d = {}
# for num in range(5):
#     t = str(num)
#     d.setdefault(t, [])
# d['0'].append('zero')
# print(d) 
# #setdefault(...) is function, so its argument will be evaluated even before it got called. So, default [] always
# #got created even on found key. On found key, [] will be discarded. On not found key, [] will be assigned to value
# #of the new key. Thus, it is wasteful if searching on big list and on key already exist.
# #In that case, use defaultdict(...) instead. Defaultdic(...) is the class accept callable(function, object) factory,
# #so, it doesn't have issue of wastefull creating and discarding [] on existed key
#===============================================================================
 
#===============================================================================
# Is there a way to introspect a function so that it shows me information on the arguments it takes (like number of args, type if possible, name of arguments if named) 
# and the return value? dir() doesn't seem to do what I want. 
# >>
# import inspect 
# print(inspect.getargspec(the_function)) 
# but help() is much better
#===============================================================================

#===============================================================================
# ###### Good STD Module 
#  import dataclasses ,collections ,itertools ,functools ,pickle ,os ,asyncio ,email ,json ,pdb ,csv, Argparse, Request
# #####
#===============================================================================

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

#===============================================================================
# num = 567
# num_weight = sum(map(int, list(str(num))))
# print(num_weight)
#===============================================================================

#===============================================================================
# List = [("lion", "ani"), ('frog', 'not mammal'), ('cat', 'tiger')]
# List2 = ["Lion is an animal", "Lion is a fish", 'Frog is not mammal', 'Cat eats Mouse', 'Tiger is a big Cat']
# ###On List2[i] not satify condition, list comp return [], it translate to False
# ###Use 0 instead of x such as[0 for s1, s2 in List if s1 in x.lower() and s2 in x.lower()] works the same
# # print(list(filter(lambda x: [x for s1, s2 in List if s1 in x.lower() and s2 in x.lower()], List2)))
# ###Generator will return all since it returns generator obj, it always translate to True
# # print(list(filter(lambda x: (x for s1, s2 in List if s1 in x.lower() and s2 in x.lower()), List2)))
# output = list(filter(lambda x: any(s1 in x.lower() and s2 in x.lower() for s1, s2 in List), List2))
# print(output)
#===============================================================================

#===============================================================================
# s = '35.555,444'
# trans = str.maketrans('.,', ',.')
# print(s.translate(trans))
#===============================================================================

#===============================================================================
# class Methods:
#     def __init__(self):
#         self.name = 'My Test Class'
#         
#     def imeth(self, x): # Normal instance method: passed a self
#         print([self, x])
#         
#     def smeth(x): # Static: no instance passed
#         print([x])
#         
#     def cmeth(cls, x): # Class: gets class, not instance
#         print([cls, x])
#         
# #     smeth = staticmethod(smeth) # Make smeth a static method (or @: ahead)
# #     cmeth = classmethod(cmeth) # Make cmeth a class method (or @: ahead
#===============================================================================

#===============================================================================
# #implement defaultdict to add missing key and count total missing key.
# #Note: this is NOT closure because counter is global and it is never going out of scope
# #    To implement closure. implement all these codes in function and change 'global counter' to 'nonlocal counter'
# from collections import defaultdict
# counter = 0 #this in main so def specify global to it to call. 
#             #If this is in def and nested def calls it, nested def need specify nonlocal NOT global to call it 
# def count_misskey():
#     global counter
#     counter += 1
#     return 0
#  
# current = {'green': 12, 'blue': 3}
# increments = [
#             ('red', 5),
#             ('blue', 17),
#             ('orange', 9),
#             ] 
# result = defaultdict(count_misskey, current)
# print('Before:', dict(result), counter)
# for key, amount in increments:
#     result[key] += amount
# print("After: ", dict(result), counter)
#===============================================================================
