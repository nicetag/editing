# -*- coding: UTF-8 -*- 
# 求交集list_common
list_a = ['a','c','q']
list_b = ['c','e','q','z']
list_common= []
for i in list_a:
    for j in list_b:
        if j == i:
            list_common.append(j)

print list_common  # ['c', 'q']

# 试着改写成求交集的函数

list_a = ['a','c','q']
list_b = ['c','e','q','z']

def common(list1,list2):
    list_common = []    
    for i in list1:
        for j in list2:
            if j == i:
               list_common.append(j)
               print list_common
    
print list_a        
print list_b            
print common(list_a,list_b)  # ['c', 'q']

