'''
Created on Aug 10, 2018

@author: hal
'''
def merge_sort(alist):
    alist_len = len(alist)
    #base case
    if alist_len <= 1:
        return alist
        
    split_point = len(alist)//2
    l_list = alist[:split_point]
    r_list = alist[split_point:]
    
    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)
        
    #merging   
    new_list = []
    i = 0
    j = 0
    
    while i < len(l_list) and j < len(r_list):
        if l_list[i] < r_list[j]:
            new_list.append(l_list[i])
            i += 1
        else:
            new_list.append(r_list[j])
            j += 1 
                
    while i < len(l_list):
        new_list.append(l_list[i])
        i += 1
        
    while j < len(r_list):
        new_list.append(r_list[j])
        j += 1    
    
    return new_list

def bubble_sort(alist, pos):
#     if len(alist) <= 1:
#         return  alist
#          
#     for i in range(len(alist)-1):
#         if alist[i] > alist[i+1]:
#             temp = alist[i]
#             alist[i] = alist[i+1]
#             alist[i+1] = temp
#     
#     blist = bubble_sort(alist[:-1])
#     blist.append(alist[-1])
#     
#     return blist

    if pos == 0 or len(alist) == 0 or len(alist) == 1:
        return
    
    for i in range(pos):
        if alist[i] > alist[i+1]:
            temp = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = temp
    
    bubble_sort(alist, pos - 1)    

def selection_sort(alist, pos):
#     if len(alist) <= 1:
#         return  alist
#     
#     #processing here
#     min_pos = 0
#     i = 1
#     while i < len(alist):
#         if alist[min_pos] > alist[i]:
#             min_pos = i
#         i += 1
#     
#     if min_pos != 0:
#         temp = alist[0]
#         alist[0] = alist[min_pos]
#         alist[min_pos] = temp             
#     
#     blist = selection_sort(alist[1:])
#     blist.insert(0, alist[0])
#     
#     return blist

    if pos == len(alist) - 1 or len(alist) <= 1:
        return
    
    min_pos = pos
    i = min_pos + 1
    while i < len(alist):
        if alist[min_pos] > alist[i]:
            min_pos = i
        i += 1
        
    if min_pos != pos:
        temp = alist[min_pos]
        alist[min_pos] = alist[pos]
        alist[pos] = temp
    
    selection_sort(alist, pos + 1)
            

unsorted_list = [21, 1, 26, 45, 29, 28, 2, 9, 106, 419, 39, 27, 43, 85, 46, 40]
# sorted_list = merge_sort(unsorted_list)
# sorted_list = bubble_sort(unsorted_list, len(unsorted_list)-1)
sorted_list = selection_sort(unsorted_list, 0)
print(unsorted_list)
