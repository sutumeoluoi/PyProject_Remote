'''
Created on Sep 1, 2018

@author: Sutu_MeoLuoi
'''

from functools import reduce
from collections import OrderedDict
#===============================================================================
# Ref:
# https://dbader.org/blog/python-first-class-functions
# https://realpython.com/primer-on-python-decorators/
#===============================================================================

#*****************************Decorator template********************************
#===============================================================================
# import functools
# 
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
# 
# @my_decorator
# def somefunc():
#     #Do something here as behavior
#===============================================================================


#===============================================================================
# def my_decorator(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     
#     return wrapper
# 
# @my_decorator
# def my_test():
#     print("this is list", repr([12, 2, 3, 4]))
#     
# my_test()
#===============================================================================
# def encryptText(aString):
#     letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     shuffled = ['h','w','r','k','f','o','i','s','y','d','q','c','x','t','l','j','m','b','g','p','e','u','z','a','n','v']
#     
#     #start with a cyphertext that is an empty string
#     cypher = ''
#     for i in range(0, len(aString)):
#         theIndex = getIndex(letters, aString[i])
#         myLetter = shuffled[theIndex]
#     cypher = cypher + myLetter
#     return cypher

# def extraLongFactorials(n):
#     fac_n = 1
#     for i in range(1, n+1):
#         fac_n = fac_n * i
#         
#     return fac_n

#===============================================================================
# def extraLongFactorials(n):
#     reduce(lambda x, y: x*y, range(1, n+1))   
# print(extraLongFactorials(25))
#===============================================================================
#===============================================================================
# scores = [100, 100, 50, 40, 40, 20, 10]
# # 
# # alice = [5, 25, 50, 120]
# 
# rank_dict = OrderedDict.fromkeys(scores, 99)    #99 is assign as value to each item of dict
# # 
# ranks = list(rank_dict) #strip duplicate   
# # al_ranks = []
# # for al_game in alice:
# #     added = False
# #     for i, rank in enumerate(ranks):
# #         if al_game >= rank:
# #             al_ranks.append(i+1)
# #             added = True 
# #             break
# #     if not added:
# #         al_ranks.append(len(ranks)+1)
# #  
# print(rank_dict)   
# print(ranks)
# print(al_ranks)
#===============================================================================

#===============================================================================
# m = map(str, [100, 100, 50, 40, 40, 20, 10] + [5, 25, 50, 120])    #map(apply func to each items of iterable. multiple iterables allow
# print(m) 
# print(list(m)) #map is iteratore, only iterate it once
# print(tuple(m))
#===============================================================================


#===============================================================================
# ### map(map obj), zip, filter return are iterator type
# input = ['Duration', 'F0', 'F1', 'F2', 'F3']
# ####Creating
# dict(zip(input, range(len(input))))
# {f: i for i, f in enumerate(input)}
# dict(map(reversed,enumerate(input)))
# ####Output
# output = {'Duration': 0, 'F0': 1, 'F1': 2, 'F2': 3, 'F3': 4}
#===============================================================================

#===============================================================================
# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  integer
# precision   ::=  integer
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
#===============================================================================
# print('{:+12,.2f}'.format(1507.89))
# print('{:<12,.2f}'.format(1507.89))
# print('{:< 12,.2f}'.format(1507.89))
# print('{:<-12,.2f}'.format(1507.89))
# print('{:v^12,.2f}'.format(1507.89))
# print('{:v<12,.2f}'.format(1507.89))
# print('{:v>12,.2f}'.format(1507.89))

#===============================================================================
# arr = [-4, 3, -9, 0, 4, 1]
# n = len(arr) 
# # pos = len([item > 0 for item in arr if item > 0]) / n
# # neg = len([item < 0 for item in arr if item < 0]) / n
# pos = sum(item > 0 for item in arr) / n
# neg = sum(item < 0 for item in arr) / n
# print('{:.6f}\n{:.6f}\n{:.6f}'.format(pos, neg, 1 - pos - neg))
#===============================================================================

#===============================================================================
# s = [1,2,3,4,5,6,7,8,9]
# n = 3
# zip(*[iter(s)]*n) # returns [(1,2,3),(4,5,6),(7,8,9)]
#===============================================================================

from itertools import chain
# n, k = 99112, 2
# n, k = 108, 2
n, k = 99714, 28288
##### TIME OUT using iter(()) and chain 3 iterators. Convert to list Using iadd fast as all working version below it ####
#===============================================================================
# output = iter(())
output = []
if not k:
    output = range(1, n+1)
# elif divmod(n, k)[1] or divmod(n, k)[0] % 2 :
elif n % (2*k):
    output = iter((-1,))
else:
    t = zip(range(1, n+1, k), range(k+1, n+2, k))    
    for i in range(n//(2*k)):
        odd, even = next(t), next(t)
#         output = chain(output, range(*even), range(*odd))    #cause TIME OUT!!!!
        output += list(range(*even)) + list(range(*odd))
#         output = (item for it in (output, range(*even), range(*odd)) for item in it)    #large number cause: RuntimeError: maximum recursion depth exceeded
 
# for item in output:
#     print(item)        
print(list(output))
#===============================================================================
# output = []
# if not k:
#     output = range(1, n+1)
# elif divmod(n, k)[1] or divmod(n, k)[0] % 2 :
#     output = iter((-1,))
# else:  
#     for i in range(n//(2*k)):
#         output += list(range(i*2*k + k+1, i*2*k + 2*k+1)) + list(range(i*2*k + 1, i*2*k + k+1)) #EXTREMELY!!! fast cauz iadd mutate list
# #         output = chain(output, range(i*2*k + k+1, i*2*k + 2*k+1), range(i*2*k + 1, i*2*k + k+1)) #much slower because add create new list everytime 
#### OR
# output = [0]*n
# if not k:
#     output = range(1, n+1)
# elif divmod(n, k)[1] or divmod(n, k)[0] % 2 :
#     output = iter((-1,))
# else:  
#     for m in range(0, n//(2*k)):
#         for i in range(1, k+1):
#             i = m*2*k + i
#             j = i - 1
#             output[j] = i+k
#             output[j+k] = i
#                            
# # print(' '.join(map(str, output)))
# print(output)

###### FROM SOMEONE ELSE ######
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     if k == 0: print(' '.join(map(str, range(1, n + 1))))
#     elif n % (2 * k) != 0: print(-1)
#     else:
#         f = []
#         for x in range(n // (2 * k)):
#             f += list(range(x * 2 * k + k + 1, x * 2 * k + 2 * k + 1)) + list(range(x * 2 * k + 1, x * 2 * k + k + 1))
#         
#         print(' '.join(map(str, f)))
########################################################

# if k == 0: print(' '.join(map(str, range(1, n + 1))))
# elif n % (2 * k) != 0: print(-1)
# else:
#     f = []
#     for x in range(n // (2 * k)):
#         f += list(range(x * 2 * k + k + 1, x * 2 * k + 2 * k + 1)) + list(range(x * 2 * k + 1, x * 2 * k + k + 1))
# print(f)         