'''
Created on Aug 2, 2018

@author: hal
'''


''' **** print each item in args list per line ****'''
def printnl(*args):
    st = '{}\n'*(len(args)-1) + '{}'
    print(st.format(*args))
''' ************************************************* '''

from functools import partial
from itertools import repeat
lines = ['"Fruits" Rob Mate Care Lost Red Pine Blue',
         'Brisk Wind Nature Dog Cat "Mouse', 
         'Butterfly Insect" "salmon" cord'
         ]

arr = ['Mate', 'Care', 'Insect', 'Mouse', 'Fruits']
linenum = 0
out = []
for line in lines:
#     linenum += 1
#     print("Line "+str(linenum) + ":", end='')
#     list = line.split()
#     for a in list:
#         if  (a in arr or
#             (a.startswith('"') and a[1:] in arr) or 
#             (a.endswith('"') and a[:-1] in arr) or 
#             (a.startswith('"') and a.endswith('"') and a[1:-1] in arr)): 
#             print ("Found", end=' ')
#         else:
#             print ("NOTFOUND",end=' ')
#     print('\n')

#     out.append(['Found' if a in arr or a.strip('"') in arr else 'NOTFOUND' for a in line.split()])

#     out.append(list(map(arr.__contains__, [st.strip('"') for st in line.split()])))
    out.append(list(map(arr.__contains__, map(str.strip, line.split(), repeat('"')) )))
printnl(*out)

# a = ['"Fruits"', 'Rob', 'Mate', 'Care', 'Lost', 'Red', 'Pine', 'Blue']
# p = map(str.strip, a, repeat('"'))
# n = list(p)
# print(n)
   
        



''' Turn multi-D list counter-clock wise 90 degree 
Output:
    [[4, 5, 6]
    [3, 3, 3]
    [2, 3, 4]
    [1, 2, 5]]
'''
#===============================================================================
# m = [[1, 2, 3, 4],
#     [2, 3, 3, 5],
#     [5, 4, 3, 6]]
#  
# # n = [[] for _ in range(len(m[0]))]
# # for item in m: 
# #     for j, x in enumerate(item[::-1]):
# #        n[j].append(x)
#  
# # n = list(map(list, zip(*m)))[::-1]          #rotate 90 degree counter-clock wise
# # n = list(map(list, map(reversed, m)))[::-1] #rotate 180 degree counter-clock wise. same as clock wise
# n = [item[::-1] for item in m][::-1]        #another implementation 180 degree counter-clock wise. same as clock wise
# # n = list(map(list, map(reversed, zip(*m)))) #rotate 90 degree clock wise
#         
# printnl(*n)
#===============================================================================


# from operator import itemgetter
# ex = ['abc', 'xyz', 'aba', '1221', 'a', '']
# # count = [item for item in ex if item and item[0])]
# # gt = itemgetter(0)
# count =list(filter(lambda x: x.endswith(gt(x)), ex))



# from timeit import timeit
''' check a list in same order in another list 
Logic: Traverse list1 and scans list2 until match. On match, next() list1 and continue scan list2 forward 
Note: using iter() and next() on list2 is best approach in this case
'''
#===============================================================================
# def consec_list(l1, l2):
#     it = iter(l2)
#     for item in l1:
#         while True:
#             try:
#                 if item == next(it):
#                     break
#             except StopIteration:   #only catch end iterator. let other exception throw
#                 return False    
#     return True
#===============================================================================

''' check a list in same order in another list -- alternative: Next() list1 and for-loop list2 ''' 
#===============================================================================
# def consec_list(l1, l2):
#     it = iter(l1)
#     try:
#         item = next(it)
#         for item2 in l2:
#             if item == item2:
#                 item = next(it)
#     except StopIteration:
#         return True
#     return False
#===============================================================================

''' check a list in same order in another list --- alternative: for-loop list1, .index() list2 '''    
#===============================================================================
# def sublist(lst1, lst2):
#     ind = 0
#     for a in lst1:
#         try:
#             ind = lst2.index(a, ind)
#         except ValueError:
#             return False
#     return True
#===============================================================================

# l1 = [15, 1, 20]*10
# l2 = [6, 1, 15, 3, 1, 6, 20]
# print(consec_list(l1, l2))
    
''' anagram: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once
Ex: ("binary", "brainy"), ("rail safety", "fairy tales")
''' 
# def is_anagram(s1, s2):   
#     return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())  
#  
# words = ("hi", "hello", "bye", "helol", "abc", "cab", 
#                 "bac", "silenced", "licensed", "decli nes")
#  
# anagram = set()
# for i, w1 in enumerate(words):
#     for w2 in words[i+1:len(words)]:
#         if is_anagram(w1, w2):
#             anagram.add(w1)
#             anagram.add(w2)
#             break
#          
# print(sorted(anagram, key=sorted))
           

''' Another implementation of anagram:
_ Build a dictionary where keys would be histograms and values would be lists of words that have this histogram.
_ For each word build it's histogram and add it to the list that corresponds to this histogram.
_ Output list of dictionary values.
Note: Counter is dict, so python <= 3.5 Counter(word).items() return not guarantee same order. 
    Using tuple(Counter(word).items()) as key of dict cause 2 different keys although same counter.
Fix: sorted() to list and convert to tuple 
Ex: different order althought same counter.
(('c', 1), ('e', 2), ('s', 1), ('d', 1), ('i', 1), ('l', 1), ('n', 1))    #silenced
(('e', 2), ('c', 1), ('d', 1), ('l', 1), ('i', 1), ('n', 1), ('s', 1))    #licensed
(('e', 2), ('n', 1), ('d', 1), ('l', 1), ('i', 1), ('c', 1), ('s', 1))    #declines
'''
#===============================================================================
# from collections import Counter, defaultdict
# def anagram(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         #histogram = tuple(Counter(word).items()) #
#         histogram = tuple(sorted(Counter(word).items())) # need sorted counter to list then convert to tuple
#         anagrams[histogram].append(word)
# #         print(histogram)
# #     printnl(anagrams)
#     return list(anagrams.values())
#  
# keywords = ("hi", "hello", "bye", "helol", "abc", "cab", 
#                 "bac", "silenced", "licensed", "declines")
#  
# print(anagram(keywords))
#===============================================================================

# for num in range(1000, 1, -1):
#     print('{}\t{}'.format(num, num if not num % 97 else '' ))

''' generator yield flow: 
each for-loop call requests countfrom() running to yield; then yield n, freeze countfrom(), return control to for-loop
'''    
#===============================================================================
# def countfrom(n):
#     while True:
#         print("before yield n= ", n)
#         yield n        
#         n += 1
#         print("after yield n= ", n)
#  
# for i in countfrom(10):
#     print("enter for loop i= ", i)
#     if i <= 10:
#         print('i= ', i)
#     else:
#         break    
#===============================================================================

''' *** @classmethod, @staticmethod and inheritance '''
#===============================================================================
# class Foo():
#   message = "I'm Foo class"
# 
#   def method(self, foo):
#     self.foo = foo
#     print(self.message)
# 
#   @classmethod
#   def class_method(cls, foo):
#     cls.foo = foo
#     print(cls.message)
# 
#   @staticmethod
#   def static_method(foo):
#     Foo.foo = foo
#     print(Foo.message)
# 
# class Bar(Foo):
#   message = "I'm Bar class"
# 
# f = Foo()
# b = Bar()
# 
# Foo.class_method(None)  # I'm Foo class
# Foo.static_method(None) # I'm Foo class
# Foo.method(Foo, None)   # I'm Foo class
# Foo.method(Bar, None)   # I'm Bar class. (Call through Foo, but passing Bar, so manipulate Bar class.
# Bar.class_method(None)  # I'm Bar class
# Bar.static_method(None) # I'm Foo class  
# Bar.method(Bar, None)   # I'm Bar class
# Bar.method(Foo, None)   # I'm Foo class. (Call through Bar, but passing Foo, so manipulate Foo class.   
# # print('***calling by instance') #output the same as call through class
# # f.class_method(None)
# # f.static_method(None)
# # b.class_method(None)
# # b.static_method(None) 
#===============================================================================

''' 
*** flatten nested list.
 Note: below work on shallow and deeper nested ['The Benchwarmers', 'Batman', 'The Avengers', ['Iron Man 1', ['Iron Man 2', 'Iron Man 3']], ['The Hulk']]
      But, NOT ['The Benchwarmers', 'Batman', 'The Avengers', [['Iron Man 1'], ['Iron Man 2', 'Iron Man 3']], ['The Hulk']]
***''' 
#===============================================================================
#  # l = ['The Benchwarmers', 'Batman', 'The Avengers', [['Iron Man 1'], ['Iron Man 2', 'Iron Man 3']], ['The Hulk']]
#  # for i, item in enumerate(l):
#  #     if isinstance(item, list):
#  #         l[i:i+1] = item
#  # print(l)
#  
# #  ####OR
# #  ''' *** list comprehension on one-level nested list. NOT work on deeper nested!!! '''
# #  l = ['The Benchwarmers', 'Batman', 'The Avengers', [['Iron Man 1'], ['Iron Man 2', 'Iron Man 3']], ['The Hulk']]
# #  n = [num for item in l for num in (item if isinstance(item, list) else (item,))]
# #  print(n)
#  
# ###OR
# from itertools import chain
# def f(item):
#    return flatten_all(item) if isinstance(item, list) else [item]
#      
# def flatten_all(alist):
#     return chain.from_iterable(map(f, alist))
#  
# l = ['The Benchwarmers', 'Batman', 'The Avengers', [[['Iron Man 1']], ['Iron Man 2'], 'Iron Man 3'], ['The Hulk']]
# n = list(flatten_all(l))
# print(n)
#===============================================================================

# from itertools import chain
# from collections import Iterable, OrderedDict
''' *** Version recursive using function, NOT generator '''
# def f(item):
# #     return [item] if not isinstance(item, Iterable) or isinstance(item, str) else flatten(item) #one-liner
#     #**Base case:
#     if not isinstance(item, Iterable) or isinstance(item, str):    
#         return [item]
#     #**Recursive
#     return flatten(item)

''' Version A: *** Work on deeper nested list. Diff from ver. B on return item instead of [item] 
chain.from_iterable() requires an iterable of iterables. If passing generator, the generator must yield iterables
on each next(). Reason: from_iterable(gen) calls next(gen), then it calls next(...) on the yield of next(gen).
Roughly equivalent implement of chain.from_iterable():
#     for it in gen:
#         for element in it:
#             yield element
In this implement,  g(itt) equivalent map(f, itt). from_iterable calls next(g) yield generator f(it).
It then calls next() on f(it) which yield [item]. 
This is where it's different from Ver. B, so this version doesn't flatten list completely. It even make worse 
on already flattened list such as [5, 6] -> [[5], [6]]. I.e, it returns 1 level deep list [[x], ...,[z]] no matter deeper level
Issue: This version implement 3-level iterables while from_iterable() only flatten 2-level iterables. 
Fix: instead of yield [item], change to yield item to reduce to 2-level iterables
Note: yield flatten(item) will yield generator obj, NOT value. Use yield from flatten(item) to force yield value
'''
#===============================================================================
# def f(item):
#     '''**Error: infinitive recursive due to yield [item] doesn't stop function as return. It jumps to yield from
#       and recursive to maximum stack error. Need to use if else'''
# #     #**Base case:
# #     if not isinstance(item, Iterable) or isinstance(item, str):    
# #         yield [item]
# #     #**Recursive
# #     yield from flatten(item)
#     '''**'''
#     if not isinstance(item, Iterable) or isinstance(item, str):
#         yield item
#     else:
#         yield from flatten(item) # equivalent: for sub in flatten(item): yield sub
# #         yield flatten(item) #cause print(n) returning generator obj flatt
# 
# def g(itt): #equivalent map(f, itt)
#     for it in itt:
#         yield f(it) 
# #         return f(it)    # only return 1st element of itt
#         
# def flatten(its):
#     gen = g(its)
#     return chain.from_iterable(gen)   
#===============================================================================

''' *** Ver. A simplify. Same as A, just using built-in map and take out comment. Read note in A '''
# def f(item):
#     if not isinstance(item, Iterable) or isinstance(item, str):
#         yield item
#     else:
#         yield from flatten(item)
#         
# def flatten(its):
#     return chain.from_iterable(map(f, its))     

''' *** Ver. A simplify, but weird!!! Need thoroughly analyze it later '''
# def f(item):
#     if not isinstance(item, Iterable) or isinstance(item, str):
#         yield [item]
#     else:
#         yield flatten(item)
#          
# def flatten(its):
#     return chain.from_iterable(chain(*map(f, its)))     
# 
# l = [ [ [ [5]]], 6, [7]]
# # l = ['The Benchwarmers','hi', [[[1]]], range(4), {99, 89}, {'a': 65, 'b': 12}, 'Batman', 'The Avengers', [[['Iron Man 1']], ['Iron Man 2', ['Iron Man 3']]], ['The Hulk']]
# n = list(flatten(l))
# print(n)         

''' Version B: *** Work on deeper nested list 
In this implement t(its), each next(t) yield [x]/generator flatten() (which is an iterable). It then calls next()
on [x] or flatten() which yield x/item or recursive yield to flatten() until reach x/item
Thus, it works to flatten all deepen nested list. It correctly returns [x, ..., z]
'''
#===============================================================================
# def t(its):
#     for x in its:
#         if not isinstance(x, Iterable) or isinstance(x, str):
#             yield [x] 
#         else: 
#             yield flatten(x)
#             
# def flatten(itera):
#     gen = t(itera)
#     return chain.from_iterable(gen)
#    
# # l = [ [5], [1, [2, 3]] ]  
# l = ['The Benchwarmers','hi', [[[1]]], range(4), {99, 89}, {'a': 65, 'b': 12}, 'Batman', 'The Avengers', [[['Iron Man 1']], ['Iron Man 2', ['Iron Man 3']]], ['The Hulk']]
# n = list(flatten(l))
# print(n)
#===============================================================================

''' *** Testing recursive generator and yield flow '''  
#===============================================================================
# # def flatten(nested, depth=0):
# #     try:
# #         print("{}Iterate on {}".format('  '*depth, nested))
# #         for sublist in nested:
# #             for element in flatten(sublist, depth+1):
# #                 print("{}got back {}".format('  '*depth, element))
# #                 yield element
# #     except TypeError:
# #         print('{}not iterable - return {}'.format('  '*depth, nested))
# #         yield nested
# #    
# # l = [ [ [5] ] ]
# # list(flatten(l))
#===============================================================================
     
''' *** generator flatten deeper nested list. NOTICE: importantly of using 'yield from' '''
#===============================================================================
# def flatten(iterable):
#     for item in iterable:
#         if isinstance(item, list) and not isinstance(item, str):  # `basestring` < 3.x
# #             yield from item          # This only flatten one level. `for subitem in item: yield item` < 3.3
#             yield from flatten(item)   # force genfunc yield items.
# #             yield flatten(item) #NOT work: return gen obj. flatten() is genfunc and only yield item on next(). For loop, list constructor, or yield from call next()
# #             flatten(item) #NOT work!!: ignore list sub-item completely            
#         else:
#             yield item
# l = ['The Benchwarmers', 'Batman', 'The Avengers', [['Iron Man 1'], ['Iron Man 2', 'Iron Man 3']], ['The Hulk']]            
# print(list(flatten(l)))
#===============================================================================

# from timeit import timeit
# print(timeit("[item for items in newlist for item in items]", "from __main__ import newlist"))
# print(timeit("sum(newlist, [])", "from __main__ import newlist"))
# print(timeit("reduce(lambda x,y: x+y, newlist)", "from __main__ import newlist; from functools import reduce"))
# print(timeit("reduce(add, newlist)", "from __main__ import newlist; from operator import add; from functools import reduce"))
# print(timeit("list(chain(*newlist))", "from __main__ import newlist; from itertools import chain"))
# print(timeit("list(chain.from_iterable(newlist))", "from __main__ import newlist; from itertools import chain"))\

''' *** list += vs .extend()
can't use += for non-local variable (variable which is not local for function and also not global)
while .extend works
'''
#===============================================================================
# def main():
#     l = [1, 2, 3]
#     def foo():
#         l.extend([4])
#     def boo():
#         l += [5]
#     foo()
#     print(l)
# #     boo()  # this will fail
# main()
#===============================================================================
    
# def getNumber(uppercaseLetter):
#     tele_pad = ["abc", "def", "ghi",  "jkl", "mno", "pqrs", "tuv", "wxyz", "0123456789"]
#     numbers = ''
#     for letter in uppercaseLetter.lower():
#         for i in range(len(tele_pad)):
#             if letter in tele_pad[i]:
#                 if i == 8:
#                     numbers += letter
#                 else:
#                     numbers += str(i+2)
#                      
#                 break                  
#     return numbers   

# def getNumber(uppercaseLetter):
#     tele_pad = ["abc", "def", "ghi",  "jkl", "mno", "pqrs", "tuv", "wxyz"]
#     tele_dict = {letter: str(i) for i, items in enumerate(tele_pad, 2) for letter in items}
#     numbers = ''.join(num if num not in tele_dict else tele_dict[num] for num in uppercaseLetter.lower())
#     
#     return numbers
     
# def run():
#     phoneNumber = input("Enter a phone number:")
#     print(getNumber(phoneNumber))
#   
# if __name__ == '__main__':
#     run()
  
# from collections import OrderedDict, ChainMap
# tele_pad = ["abc", "def", "ghi",  "jkl", "mno", "pqrs", "tuv", "wxyz"]
# tele_cm = ChainMap()
# # tele_dict = OrderedDict()
# for i, pad in enumerate(tele_pad, 2):
# #     tele_dict.update(dict.fromkeys(pad, i))
#     tele_cm = tele_cm.new_child(dict.fromkeys(pad, i))
# print(tele_cm)

# c = ChainMap()
# d = c.new_child()
# e = d.new_child()
# print(e)
        
# from itertools import repeat
# t = iter(range(ord('a'), ord('z')+1))
# t1 = iter(range(2, 10))
# print(list(zip(zip(t, t, t), (t1,)*3)))

# nums = [0, 3, 2, -95, 0, False, -5, 1, 0.00, 3, 4]
# nums.sort(key=lambda x: x is not False and x == 0)
# print(nums)

''' **** why dict.fromkeys() sorted in this case? '''
#===============================================================================
# from random import shuffle
# a = list(range(0,5))*2
# shuffle(a)
# print(a)
# print(dict.fromkeys(a).keys()) #dict_keys([0, 1, 2, 3, 4]). why sorted?
#===============================================================================

''' **** Remove duplicate item and retain list current order **** '''
#===============================================================================
# ### Python < 3.6. NOTE: NOT work if list item is NOT hashable
# from collections import OrderedDict
# t = [1, 2, 9, 58, 15, 3, 1, 2, 5, 6, 7, 8]
# od = OrderedDict.fromkeys(t)
# ### Python >= 3.6. Regular dict is now having insertion order
# # od = dict.fromkeys(t)
# print(list(od))
#===============================================================================
 
''' ###OR: hacking way and list  comprehension. Work on un-hashable items
###Note: can't use tuple such as (x,) or ([11],). Although tuple is immutable, [11] in it is mutable so hash value could NOT created.
tuple as a key if all elements in it are immutable. If the tuple contains mutable objects, it cannot be used as a key. 
Thus, a tuple to be used as a key can contain strings, numbers, and other tuples containing references to immutable objects.
'''
#===============================================================================
# seq = [1, 2, 9, [11], 58, 15, [11], 3, 1, 2, 5, 6, 7, 8]
# seen = set()
# l = [x for x in seq if str(x) not in seen and not seen.add(str(x))]
# print(l)
#===============================================================================


''' **** Consume whole iterator without using it **** '''
#===============================================================================
#  collections.deque(iterator, maxlen=0) #deque consume whole iterator, but never keep any item due to maxlen=0
#===============================================================================

#===============================================================================
# l=[1, 2, 3, 99, 65, 8656, 896, 23]
# it = reversed(l)
# for first, second in zip(l, it):
#     print(first, second)
#===============================================================================

'''
islice consumes iterator and throw-away elements to 'start' position. Then, create slice to 'stop' position.
after islice done. The current position of iterator will be at max(start, stop). ie., at either greatest
On 'step' over 'stop', slice won't reach 'stop', but iterator will consume(move) to 'stop'
'''
#===============================================================================
# import itertools
# print([x*2 for x in range(10)])
# ge = (x*2 for x in range(10))
# # it = itertools.islice(ge, 6, 3, None) #empty slice. Move iterator to position 6
# it = itertools.islice(ge, 3, 5, 3) #slice=[6], next step over 'stop'. Move iterator to postion 'stop'(5)
# print(list(it))
# print(list(ge))
#===============================================================================
    
''' **** l[n] - l[n-1] '''
#===============================================================================
# l=[1, 22, 3, 99, 65]
# # import operator, itertools
# # print(list(map(operator.sub, l[1:], l)))
# 
# ###OR
# it = itertools.islice(l, 1, None, None)
# print(list(map(operator.sub, it, l)))
# 
# ###OR
# it = itertools.islice(l, 1, None, None)
# print([next - curr for next, curr in zip(it, l)])
#===============================================================================
        

# a = (item*2 for item in range(6))
# print(a)
# print(sorted(a, reverse=True))

#===============================================================================
# # from operator import itemgetter
# # a = {(0, 0): 'a', (1, 1): 'd', (0, 1): 'b', (1, 0): 'c'}
# # a_keys_sorted = sorted(a)
# # b = [a[k1]+a[k2] for k1, k2 in zip(a_keys_sorted[::2], a_keys_sorted[1::2])]
# # print(b)
# # print(list(a))
# # print(a_keys_sorted)
# # 
# # ###### OR
# # t = iter(sorted(a.items()))
# # getter = itemgetter(1)
# # # b = [getter(next(t)), getter(next(t))]
# # # b = [d1[1] + d2[1] for d1, d2 in zip(t, t)]
# # b = [getter(v1) + getter(v2) for v1, v2 in zip(t, t)]
# # print(b)
#  
# ###### OR
# a = {(0, 0): 'a', (1, 1): 'd', (0, 1): 'b', (1, 0): 'c'}
# t = iter(sorted(a.items()))
# # print(next(t), next(t))
# b = [v1+v2  for (k1, v1), (k2, v2) in zip(t, t)] #zip return outer tuple 2 items. each item again inner tuple 2 item (((0, 0), 'a'), ((0, 1), 'b'))
#                 #so, need unpack outer tuple. then unpack inner tuple to (k, v). K is also tuple, but no need process k, so not gonna unpack further
# ###### OR 
# # b = [d1[1] + d2[1] for d1, d2 in zip(t, t)]
# print(b)  
#  
# # ###### OR
# # a = {(0, 0): 'a', (1, 1): 'd', (0, 1): 'b', (1, 0): 'c'}
# # t = iter(sorted(a))
# # b = [a[d1] + a[d2] for d1, d2 in zip(t, t)]
# # print(b)    
#===============================================================================

''' **** Itertools.tee() CAUTION!!! '''
''' tee() create n independent iterators, each iterator is essentially working with its own FIFO queue.
When a value is extracted from one iterator, that value is appended to the queues for the other iterators. 
Thus, if one is exhausted before others, each remaining iterator will hold a copy of the entire iterable in memory
'''

''' **** Implement FIRST ORDER RECURRENCE logic using accumulate **** '''
#===============================================================================
# import itertools as itr
# def first_order(p, q, initial_val):
#     """Return sequence defined by s(n) = p * s(n-1) + q."""
#     return itr.accumulate(itr.repeat(initial_val), lambda s, _: p*s + q)
# 
# evens = first_order(p=1, q=2, initial_val=0)
# a = list(next(evens) for _ in range(5))
# ##[0, 2, 4, 6, 8]
# 
# odds = first_order(p=1, q=2, initial_val=1)
# b = list(next(odds) for _ in range(5))
# ##[1, 3, 5, 7, 9]
# 
# count_by_threes = first_order(p=1, q=3, initial_val=0)
# c = list(next(count_by_threes) for _ in range(5))
# ##[0, 3, 6, 9, 12]
# 
# count_by_fours = first_order(p=1, q=4, initial_val=0)
# d = list(next(count_by_fours) for _ in range(5))
# ##[0, 4, 8, 12, 16]
# 
# all_ones = first_order(p=1, q=0, initial_val=1)
# e = list(next(all_ones) for _ in range(5))
# ##[1, 1, 1, 1, 1]
# 
# all_twos = first_order(p=1, q=0, initial_val=2)
# f = list(next(all_twos) for _ in range(5))
# ##[2, 2, 2, 2, 2]
# 
# alternating_ones = first_order(p=-1, q=0, initial_val=1)
# g = list(next(alternating_ones) for _ in range(5))
# ##[1, -1, 1, -1, 1]
# 
# # printnl(*(chr(i) for i in range(ord('a'), ord('g')+1))) # NOT Work
# printnl(*((globals()[chr(i)] for i in range(ord('a'), ord('g')+1)))) #globals() return all symbols in global __dict__
# # printnl(a, b, c, d, e, f, g)
#===============================================================================

''' **** print list previous, current, next item '''
#===============================================================================
# l=[1,2,3, 99, 65, 8656, 'me', 896, 23]
# for prev,cur,next in zip([None]+l[:-1], l, l[1:]+[None]):
#     print(prev,cur,next)
#===============================================================================

''' **** print list current, next item **** '''
# l=[1, 2, 3, 99, 65, 8656, 896, 23]
#  for i, j in zip(l, l[1:]):
#      print(i, j)
##OR
#  for i in range(len(l)-1):
#      print(l[i], l[i+1])
##OR
# for (i, curr) in enumerate(l[:-1]):
#     print(curr, l[i+1])
##OR
#  def pairwise(iterable):
#      it = iter(iterable)
#      a = next(it, None)
#      for b in it:
#          yield (a, b)
#          a = b
#  print(list(pairwise(l)))
##OR
#  import itertools
#  def pairwise(iterable):   
#      a, b = itertools.tee(iterable)
#      next(b, None)
#      return zip(a, b)
#  print(list(pairwise(l)))
    
'''****Count occurences in list'''
#===============================================================================
# from collections import Counter
# from collections import defaultdict
#  
# mylist=[1,1,1,1,1,1,2,3,2,2,2,2,3,3,4,5,5,5,5]*10
#  
# def s1(mylist): 
#     return {k:mylist.count(k) for k in set(mylist)}
#  
# def s2(mlist):
#     return Counter(mylist)
#  
# def s3(mylist):
#     mydict=dict()
#     for index in mylist:
#         mydict[index] = mydict.setdefault(index, 0) + 1
#     return mydict   
#  
# def s4(mylist):
#     mydict={}.fromkeys(mylist,0)
#     for k in mydict:
#         mydict[k]=mylist.count(k)    
#     return mydict    
#  
# def s5(mylist):
#     mydict={}
#     for k in mylist:
#         mydict[k]=mydict.get(k,0)+1
#     return mydict     
#  
# def s6(mylist):
#     mydict=defaultdict(int)
#     for i in mylist:
#         mydict[i] += 1
#     return mydict       
#  
# def s7(mylist):
#     mydict={}.fromkeys(mylist,0)
#     for e in mylist:
#         mydict[e]+=1    
#     return mydict    
#  
# if __name__ == '__main__':   
#     import timeit 
#     n=1000000
#     print(timeit.timeit("s1(mylist)", setup="from __main__ import s1, mylist",number=n))
#     print(timeit.timeit("s2(mylist)", setup="from __main__ import s2, mylist, Counter",number=n))
#     print(timeit.timeit("s3(mylist)", setup="from __main__ import s3, mylist",number=n))
#     print(timeit.timeit("s4(mylist)", setup="from __main__ import s4, mylist",number=n))
#     print(timeit.timeit("s5(mylist)", setup="from __main__ import s5, mylist",number=n))
#     print(timeit.timeit("s6(mylist)", setup="from __main__ import s6, mylist, defaultdict",number=n))
#     print(timeit.timeit("s7(mylist)", setup="from __main__ import s7, mylist",number=n))
# '''   
# ********** RESULT ***********
# 1. 27.912882882080456
# 2. 20.123256369280778
# 3. 47.757165042503054
# 4. 28.73874751076798
# 5. 47.79526024672896
# 6. 25.16641805965054
# 7. 29.540249596749277
# '''
#===============================================================================

#===============================================================================
# st = 'lolabbcdtellllc'
# # result = {ch for i, ch in enumerate(st) if st.find(ch, i+1) != -1}
# # print(result)
# 
# for i, ch in enumerate(st):
#     if st.find(ch, i+1) != -1:
#         print(ch)
#         break
#===============================================================================

''' **** sorted dictionary to list '''
#===============================================================================
# dic1 = {'first': 13, 'third': 5, 'second': 7,}
# sortlist = sorted(dic1.values(), reverse=True)
# sortlist1 = sorted(dic1.keys(), reverse=True)
# sortlist2 = sorted(dic1, reverse=True) #same as above
# sortlist3 = sorted(dic1, key=dic1.get, reverse=True) #sorted by values, output: keys
# sortlist4 = sorted(dic1.items(), reverse=True)
# printnl(sortlist, sortlist1, sortlist2, sortlist3, sortlist4)

''' **** find max value in dict '''
#===============================================================================
# from operator import itemgetter
# dic1 = {'first': 13, 'second': 7, 'third': 5}
# mx = max(dic1, key=dic1.get)    #output: 'first'
# mx2 = max(dic1.items(), key=itemgetter(1)) #output: '{'first', '13'}
# mx3 = max(dic1.items(), key=itemgetter(1))[0] #output: 'first'
# printnl(mx, mx2, mx3)
#===============================================================================

''' ****filter specific value from list
**using None in function of filter apply id test as 'lambda x: x' or 'is' test
'==' is an equality test. It checks equal objects (according to their __eq__ or __cmp__ methods.)
'is' is an identity test. It checks the very same object. No method calls are done, objects cannot influence the 'is' operation.
use 'is' (and 'is not') for singletons, like None, where don't care about objects that might want to pretend to be None 
or where you want to protect against objects breaking when being compared against None
'''
#===============================================================================
# a = [1, 2, 3, None, 0, [], 86469]
# b = [x for x in a if x is not 86469] #failed to ignore 86469 cause 'is not' id test 86469 check on obj. 
#         #obj 86469 in list comp is different obj in a. for -255 to 255, python creates constant obj so will ignore fine.
# y = 0
# c = list(filter(y.__ne__, a))
# d = list(filter(None, a))
# e = [x for x in a if x != None]
# printnl(a, b, c, d, e)
# # print(max(a, b, default=0)) #Python 3: TypeError: unorderable types: NoneType() > int(). same as [] inside the list
# #                 #default also NOT work on multiple iterables
# print(max(filter(lambda x: x not in (None, []), [None, None])) if any([None, None]) else None) #fix TypeError above
# max([] or [99]) #ver < 3.4
#===============================================================================

''' ***Insert list b to 'i' position of list a '''
# list_a[i:i] = list_b

''' ***Insert list b in front list a '''
#===============================================================================
##!!Hettinger: should consider collections.dequeue
# list_a = list_b + list_a
# 
# for item in list_b:
#     list_a.insert(0, item)
#     ##!!Hettinger: should consider collections.dequeue
# 
# for item in self.list_a:
#     list_b.append(item)
# 
# list_a = list_b
# 
# list_a[0:0] = list_b
#===============================================================================

#===============================================================================
# from itertools import accumulate
# def find_mean(a,q):
#     lr = ['1 3', '2 4', '2 5']
#     for item in lr:
# #     for _ in range(q):
# #         lr = input()
#         l,r = map(int,item.split())
#         k = a[l-1:r]
# #         print(type(k))
#         print(sum(k)//len(k))
#     
# 
# # nq = input()
# # arr = input()
# nq = '5 3'
# arr = '1 15 2 99 4 5'
# n,q = map(int,nq.split())
# arr_int = list(map(int, arr.split()))
# arr_sums =[0]
# arr_sums.extend(list(accumulate(arr_int)))
# 
# print(arr_sums)
# lr = ['1 3', '2 4', '2 5', '3 6']
# sum_a = []
# sum_b = []
# for item in lr:
#     l,r = map(int,item.split())
#     sum_a.append(sum(arr_int[l-1:r]))
#     sum_b.append(arr_sums[r] - arr_sums[l-1])
# print(sum_a) 
# print(sum_b)
#===============================================================================
 
#===============================================================================
#import re
#from functools import reduce
## G = '11'
## P = '11111'
## founds = re.finditer(r'(?=' + P + ')', G)
## result = [found.start() for found in founds]
## print(result)

# def gridSearch(G, P):   
#     delta_len = len(G) - len(P)
#     match_list = []
#     for i, st1 in enumerate(G):
#         if i < delta_len:
#             matches = re.finditer(r'(?=' + P[0] + ')', st1)
#             result = [a_match.start() for a_match in matches]         
#             if result:
#                 match_list.append(result)
#                 break
#     else:    
#         return 'NO'
#            
#     for st1, st2 in zip(G[i+1:], P[1:]):        
#         matches = re.finditer(r'(?=' + st2 + ')', st1)
#         result = [a_match.start() for a_match in matches]         
#         if not result:
#             return 'NO'        
#         match_list.append(result)
#     
#     answer_list = list(reduce(lambda x, y: x & y, map(set, match_list)))
#          
#     return 'YES' if answer_list else 'NO'
#   
#   
# t = int(input())
#   
# for t_itr in range(t):
#     RC = input().split()
#   
#     R = int(RC[0])
#   
#     C = int(RC[1])
#   
#     G = []
#   
#     for _ in range(R):
#         G_item = input()
#         G.append(G_item)
#   
#     rc = input().split()
#   
#     r = int(rc[0])
#   
#     c = int(rc[1])
#   
#     P = []
#   
#     for _ in range(r):
#         P_item = input()
#         P.append(P_item)
#   
#     result = gridSearch(G, P)
#   
#     print(result)
#===============================================================================
         
# dictlist = [{'label':'240p','url':'url'}, {'label':'720p','url':'url'},{'label':'480p','url':'url'}]
# print(max(dictlist, key=lambda x: x['label'])['label'])

''' ****Find next lexicographical permutation 
ref: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
1. Find largest index i such that array[i - 1] < array[i]
   (from rightmost, find largest(size) subset in increasing order right to left. ex: [5, 4] of [2, 3, 5, 4]
   Pivot = 3, max_of_subset = 5. Keep their indices. If no such i exists, then this is already the last permutation.)
2. Find largest index j such that j >= i and array[j] > array[i - 1].
   (On found subset, from rightmost, find item > pivot. keep its index. 
   Subset already ordered right to left, so item is the smallest item and > pivot)
3. Swap array[j] and array[i - 1].
4. Reverse the suffix starting at array[i].
Note: step 4 could use sorted() or reversed() because sublist already sorted and swapping still keep it sorted
'''
#===============================================================================
# def check_bigger(a):
#     for i in range(-1, -len(a), -1):
#         if a[i] > a[i-1]:
#             max_i = i       
#             pivot = a[i-1]
#             break
#     else:        
#         return 'no answer'
#       
#     sub_list = list(a[max_i:])
#     for j in range(-1, -(len(sub_list)+1), -1):
#         if sub_list[j] > pivot:
#             sub_list[j], pivot = pivot, sub_list[j]
#             break
#              
#     return a[:max_i-1] + str(pivot) + ''.join(sorted(sub_list))
#       
# a = ['lmno', 'dcba', 'dcbb', 'abdc', 'abcd', 'fedcbabcd', 'zedawdvyyfumwpupuinbdbfndyehircmylb']
# for item in a:
#     print(check_bigger(item))
#===============================================================================
     
''' *** Check repeated char string '''
#===============================================================================
# import re
# def test_regex(s,regex=re.compile(r'^(.)\1*$')):
#     return bool(regex.match(s))
# 
# def test_all(s):
#     return all(x == s[0] for x in s)
# 
# def test_count(s):
#     return s.count(s[0]) == len(s)
# 
# def test_set(s):
#     return len(set(s)) == 1
# 
# def test_replace(s):
#     return not s.replace(s[0],'')
# 
# def test_translate(s):
#     return not s.translate(None,s[0])
# 
# def test_strmul(s):
#     return s == s[0]*len(s)
# 
# #**Result
# # WITH ALL EQUAL
# # test_all 5.83863711357
# # test_count 0.947771072388
# # test_set 2.01028490067
# # test_replace 1.24682998657
# # test_translate 0.941282987595
# # test_strmul 0.629556179047
# # test_regex 2.52913498878
# # 
# # WITH FIRST NON-EQUAL
# # test_all 2.41147494316
# # test_count 0.942595005035
# # test_set 2.00480484962
# # test_replace 0.960338115692
# # test_translate 0.924381017685
# # test_strmul 0.622269153595
# # test_regex 1.36632800102
#===============================================================================

# alist = [1, 7, 3, 9, 2]
# # alist = [3, 7, 1, 9, 2]
# # alist = [6, 7, 1, 5]
# min_item = min(alist)
# min_i = alist.index(min_item)
# max_item = max(alist[min_i+1:])
# print(max_item - min_item)    
    
# # triplet_list = [chr(i)*3 for i in range(ord('a'),ord('z')+1)]
# # print(triplet_list)
# # check_str = 'aaaaabcdefghhh'
# # count_triplet = list(map(check_str.count, triplet_list))
# # print(count_triplet)
# 
# import re
# 
# # check_str = 'aaaabbbcdeeeefghhhaaa'
# # pat = r'(\w)(?<!\1)\1{2}(?!\1)'
# # reg_obj = re.compile(pat, re.S)
# # ## triplet = reg_obj.match(check_str)
# # ## print(triplet)
# # counter = [_ for _ in reg_obj.finditer(check_str)]
# # print(counter)
# # # counter = [1 for _ in reg_obj.finditer(check_str)]        
# # # print(sum(counter))
# # # list_triplet = re.findall(pat, check_str)
# # # print(list_triplet)
# 
# p = re.compile(r'(\w)\1\1(?<!\1\1\1\1)')
# #r'(?<=(?=(.)\1\1)...)'
# check_str = 'aaaaabcdeeeefghhhaaa'
# # matches = re.findall(p, check_str)
# matches = re.search(p, check_str)
# print(matches.start(), matches.end())
# print(check_str[matches.start():matches.end()])


# d = {
#     'Woody': lambda x: x1 - 30,
#     'Herbaceous': 31 - 85,
#     'Algae': 86 - 90,
#     'Fungus': 91 - 100,
#     }
# roll = 5
# if roll in range(1, 30):
#     pass
# elif roll in range(31, 85):
#     pass
# elif roll in range(86, 90):
#     pass
# elif roll in range(91, 100):
#     pass

''' *** Nested tuple unpacking '''
#===============================================================================
# floraTypes = {'woody': [1,30], 'herby': [31,85]}
# num = 31
# for t, (start, end) in floraTypes.items():
#     if start <= num <= end: 
#         print(t)
#===============================================================================

#===============================================================================
# from itertools import cycle, chain, combinations, tee
# import timeit
# 
# nums = [-1, 0, 1, 2, -1, -4, -9, 4, -5, 7, 8, -3, -2, 6]*100
# nums = sorted(set(nums))
# 
# start_time = timeit.default_timer()
# # print(len(nums))
# # get triplet tuples
# lc = combinations(nums, 3)
#    
# # keep only those triplets that sum to 0
# # lf = filter(lambda x: sum(x) == 0, lc)
# lsum = sum
# lsorted = sorted
# lf = (lsorted(item) for item in lc if not lsum(item))
# # print(timeit.default_timer() - start_time)
# # sort each triplet because (-1,0,1) == (-1,1,0)
# # and we need unique triplets only
# # lfms = map(sorted, lf)
# # lfms = (lsorted(item) for item in lf)
# # lfms = map(lambda x: tuple(sorted(x)), lf)
#    
# # now, add to result list only unique triplets
# # that sum to 0
#    
# # s = []
# # for t in lf:
# #     if t not in s:
# #         s.append(t)
#    
# lfms = map(tuple, lf)
# s = set(lfms)
# print(s)
# print(len(s))
# print(timeit.default_timer() - start_time)
#  
# start_time = timeit.default_timer()
# def find_3sum(arr):
#     sum3_list = set()
#     for i, item in enumerate(arr):
#         j = i + 1
#         sum = -item
#         k = len(arr) - 1
#         while j < k:
#             sum2 =  arr[j] + arr[k]
#             if sum == sum2:
#                 sum3_list.add((item, arr[j], arr[k]))
#                 j += 1
#                 k -= 1
#                 while arr[j] == arr[j-1]:
#                     j += 1
#             elif sum > sum2:
#                 j += 1
#             else:
#                 k -= 1
#     return sum3_list
#     
# nums.sort()
# trip_set = find_3sum(nums)
# print(sorted(list(trip_set)), '\n', len(trip_set))
# print(timeit.default_timer() - start_time)
# 
# print(s == trip_set)
#===============================================================================

''' *** in this case array.array slower than list '''
#===============================================================================
# import array
# import timeit
# start_time = timeit.default_timer()
# nums = [5, 7, 2, 9, 12, 4, 65, 35, 1, 89]*100000
# sort_arr = sorted(nums)
# # num_arr = array.array('i', nums)
# # sort_arr = sorted(num_arr)
# # print(sort_arr)
# print('final', timeit.default_timer() - start_time)
#===============================================================================

# server1 = ['a','b','c']
# server2 = ['d','e','f']
# server3 = ['g','h','i']
# server_names = chain.from_iterable(zip(server1, server2, server3)) 
# print(list(server_names))

''' *** Remove 0 in sub-list '''
#===============================================================================
# L = [[5, 0, 6], [7, 22], [0, 4, 2], [9, 0, 45, 17]]
# # L = [list(filter(lambda x: x != 0,item)) for item in L]
# # L = [list(filter(None,item)) for item in L] #None defaulted to use identity funct where false item return false. in this case 0 is false
# # L = list(map(lambda y: list(filter(lambda x: x != 0, y)) , L))
# L = [[subitem for subitem in item if subitem] for item in L]    #using nested conditional list comprehension taking advantage of 0 is false
# print(L)
#===============================================================================

''' ****** SINGLETON Design Pattern '''
#===============================================================================
# # Standard singleton design pattern, for most languages, to ensure that only one instance of 
# # the class is ever created. An implementation of the singleton pattern must:
# # _ ensure that only one instance of the singleton class ever exists; and
# # _ provide global access to that instance.
# # ***
# # The constructor says:
# # If there is no instance recorded, 
# #    create an instance and record it
# # return the recorded instance
# # ***
# #### Method 1: Using base class method
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
# ################################################### 
# #### Method 2: Using metaclass method
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls] 
# ##Python2
# class MyClass(BaseClass):
#     __metaclass__ = Singleton 
# ##Python3
# class MyClass(BaseClass, metaclass=Singleton):
#     pass
# ###################################################
# #### Method 3: 
# # Other methods: using class decorator(define function to decorate class, at the end class turn into function
# #### Method 4: Encapsulate class and declare an instance of class in same module. Import module.
# ####    Import only happens once, so there is only one instance exist.
# #Put these code in mysingleton.py
# #>>>>>>>>>
# class My_Singleton(object):
#     def foo(self):
#         pass
# my_singleton = My_Singleton()   #a global instance of My_Singleton obj in mysingleton module 
# #>>>>>>>>>
# #on using
# from mysingleton import my_singleton
# my_singleton.foo()
# # *******************
#===============================================================================


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


''' ***Create/copy list of mutable object*** 
* remember that repetition, concatenation, and slicing copy only the top level of their operand objects
* L1, L2, X,board,... is reference to list object [2, 3, 4], [4, 5, 6],... Thus, any repetition, concatenation
of them just clone them(clone reference), NOT clone the object. It will create multiple copies of the same
object.
'''
#===============================================================================
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

''' ******CLOSURE******
* A closure is a function remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope
* A function object remembers values in enclosing scopes regardless of whether those scopes are still present in memory
* A functions that refer to variables from the scope in which they were defined
* A function with an extended scope that encompasses nonglobal variables referenced in the body of the function 
but not defined there. It does not matter whether the function is anonymous or not; what matters is that it can access nonglobal
variables that are defined outside of its body. closures only matter when you have nested functions.
* A nested function that accesses values from outer local variables is also known as a closure
'''
#===============================================================================
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

'''*** lambda TRAP!!! ***
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
'''

# lds = []
# for x in range(6):
#     lds.append(lambda: x + 2)
# x = 10
# print([ld() for ld in lds])

'''
### assign x = 0 after list comprehension NOT change return value of lambda. Lambda got closure on x with the lastes value = 5 and 
### calculate to return 7 on every lambda object
'''
# lds = [lambda: x + 2 for x in range(6)]
# x = 10
# print([ld() for ld in lds])
# print(lds[0]())
# print(lds)

'''
list comprehension leak 'x' into outside scope in python 2. However, Python 3 fixed it.
Thus, python 2 will print '6' and python 3 will error "name 'x' is not defined"
Ref: https://stackoverflow.com/questions/4198906/python-list-comprehension-rebind-names-even-after-scope-of-comprehension-is-thi
'''
#===============================================================================
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

'''    
ATTENTION!!!: A = ((X and Y) or Z). Always try to evaluate to True and return the latest item when it stop
Semantic: evaluate left to right 
    1. On X true, evaluate Y; on Y true stop evaluation since next is 'or'. So return Y.  
    2. On X false, not going to Y, jump to evaluation Z. Either Z True or False, always return Z bcauz Z is the last item
    3. On X true, evaluate Y; on Y false, evaluate Z and return Z since Z is the last item. (CAN'T use replace an if else)
Note: 1 and 2 can use to replace ternary Y if X else Z. 3 can't use since it return Z on X true and Y false.
    I.e, only use it to replace Y if X else Z when you are sure Y always TRUE!!!!
'''

'''
setdefault(...) is function, so its argument will be evaluated even before it got called. So, default [] always
got created even on found key. On found key, [] will be discarded. On not found key, [] will be assigned to value
of the new key. Thus, it is wasteful if searching on big list and on key already exist.
In that case, use defaultdict(...) instead. Defaultdic(...) is the class accept callable(function, object) factory,
so, it doesn't have issue of wastefull creating and discarding [] on existed key
'''
#===============================================================================
# d = {}
# for num in range(5):
#     t = str(num)
#     d.setdefault(t, [])
# d['0'].append('zero')
# print(d) 
#===============================================================================
 
'''
Is there a way to introspect a function so that it shows me information on the arguments it takes (like number of args, type if possible, name of arguments if named) 
and the return value? dir() doesn't seem to do what I want. 
>>
import inspect 
print(inspect.getargspec(the_function)) 
but help() is much better
'''

''' ###### Good STD Module 
 import dataclasses ,collections ,itertools ,functools ,pickle ,os ,asyncio ,email ,json ,pdb ,csv, Argparse, Request
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

''' *** 'candle' becomes 'ACDNEL' '''
#===============================================================================
# word = 'candleg'
# new_word = ''.join(word[i:(i+2)][::-1] for i in range(0, len(word), 2)).upper() #join accept iterables(list, tuple, generator, iterator...)
# print(new_word)
#===============================================================================

#===============================================================================
# with open("in-out.txt", "r") as f:
#     read_list = [line.rstrip('\n') + " is an excellent webcomic\n" for line in f]
# print(read_list) 
#  
# with open("in-out.txt", "w") as f:
#     f.writelines(read_list)
#===============================================================================

''' ***populate 2d list from user input '''
#===============================================================================
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

'''
implement defaultdict to add missing key and count total missing key.
Note: this is NOT closure because counter is global and it is never going out of scope
    To implement closure. implement all these codes in function and change 'global counter' to 'nonlocal counter'
'''
#===============================================================================
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
