'''
Created on Aug 18, 2018

@author: hal
'''
# from threading import Thread
# import queue
# 
# 
# def run_input(q):
#     line_of_text = input()
#     q.put(line_of_text)
# #     print(line_of_text)
#         
# q = queue.Queue()
# 
# print("Enter some text and press enter: ")
# thread = Thread(target=run_input, args=(q, ))
# thread.start()
# 
# count = result = 1
# while thread.is_alive():
#     result = count * count
#     count += 1
#     
# thread.join()
#     
# print("calculated squares up to {0} * {0} = {1}".format(count, result))
# print("while you typed '{}'".format(q.get()))

org = ['inter', 'ca', 'ak', 'hi', 'or', 'qu1', 'qu2', 'qu3', 'pm1', 'pm2', 'pm3', '/*c', 'gq1', 'gq2*/', 'gq12']
holder = [org.index(item) for item in org if item[:2] == '/*' or item[-2:] == '*/']

for i in range(len(org):
    if org[i].startswith('/*'):
        start_del = i
    elif org[i].startswith('/*'):
        end_del = j
         


print(org)
print(holder)

for i in range(0, len(holder), 2):
    for j in range(holder[i], holder[i+1]):
        del org[j]
        print(org)
        
print(org)        
len(org)
# [del org[j] for i in range(0, len(holder), 2) for j in range(holder[i], len(org))]