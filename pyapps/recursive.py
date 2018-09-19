'''
Created on Aug 7, 2018

@author: hal
'''
'''
def print_arr(arr, pos):
    #base case
    if pos == len(arr) - 1:
        print(arr[pos]) 
        return
    
    #recursive case
    print_arr(arr, pos + 1 )
    print(arr[pos])
    return
    
arr = [6, 1, 9, 3, 5, 2]
print_arr(arr, 0)    
'''

# def is_palin(st):
#     if len(st) <= 1:
#         return True
#     
#     if (st[0] == st[len(st)-1]):
#         return is_palin(st[1:-1])
#     
#     return False
# 
# print(is_palin("121321"))
# print(is_palin("aa"))
# print(is_palin("mamam2"))

