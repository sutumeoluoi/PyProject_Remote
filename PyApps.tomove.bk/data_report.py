'''
Created on Aug 19, 2018

@author: Sutu_MeoLuoi
'''
import re

# def strip_string(a_str):    
#     x = 0
#     y = 0
#     for i in range(len(a_str)):
#         if a_str[i].startswith('/*'):
#             x = i
#         elif a_str[i].endswith('*/'):
#             y = i
#             break
#          
#     if x == 0 or y == 0:
#         return 
#     
#     del a_str[x:y+1]
#     strip_string(a_str) 

def filter_string(a_list):
    x = 0
    y = 0
    for i, item in enumerate(a_list):
        if item.startswith('/*'):
            x = i
        elif item.endswith('*/'):
            y = i
            break
    
    if x == 0 or y == 0:
        return 
    
    del a_list[x:y+1]
    filter_string(a_list) 
    
    
            
org_list = ['inter', 'ca', 'ak', 'hi', 'or', '/*qu1', 'qu2', 'qu3', 'pm1*/', 'pm2', 'pm3', '/*c', 'gq1', 'gq2*/', 'gq12']

# regex = re.compile(r'[a-zA-Z0-9]+?')
# new_list = [item for item in org_list if regex.search(item)]
# new_list = []
# for item in org_list:
#     if regex.search(item):
#         new_list.append(item)
# print(new_list)

print(org_list)
filter_string(org_list)
print(org_list)

# [del org[i:j for j in len(org) if org[j].endswith('*/')] for i in len(org) if org[i].startswith('/*')]