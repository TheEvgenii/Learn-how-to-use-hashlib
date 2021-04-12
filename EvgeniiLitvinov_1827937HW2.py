#
#  EvgeniiLitvinov_1827937HW2.py
#  Evgenii_Litvinov_HM2
#  COSC3371 
#  Purpouse for the assigment: Learn how to use hashlib.
#  Code was written in Python3.0 language
# Created by Evgenii Litvinov on 04/5/21.
#


import hashlib
import time

#2.1

#1
start_time = time.time()
with open('users.txt') as file_two:
    file_two.readline()
    data_two = file_two.readline()

s = data_two.split(",")
username = s[0]
h = s[1]
h = h[:-1]

file_one =  open('password_dictionary.txt', 'r')
data_one = file_one.readlines()
for line in data_one:
    data = line[:-1]
    password = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
    if (h==password):
        print(data)
print("--- %s seconds ---" % (time.time() - start_time))

#2.2

start_time = time.time()
p_dict = {}
with open('users.txt') as file_two:
    file_two.readline()
    data_two = file_two.readline()    
               
file_one =  open('password_dictionary.txt', 'r')
data_one = file_one.readlines()
for line in data_one:
    data = line[:-1]
    password = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
    p_dict[data] = password

for line in data_two:
    s = data_two.split(",")
    h = s[1]
    h = h[:-1]
    for key, value in p_dict.items():
        if (h==value):
            print("--- %s seconds ---" % (time.time() - start_time))
    break

#2.3

#4
#start_time = time.time()
#list1 = []
#list2 = []

#with open ("users.txt") as myfile:
#    for line in myfile:
#        x1,x2 = map(str,line.split(','))
#        list1.append(x1)
#        list2.append(x2)
#my_list=list2
# 
#duplicates=[]
#for i in my_list:
#     if my_list.count(i)>1:
#         if i not in duplicates:
#             duplicates.append(i)
#             break 
#print(duplicates)

#5
password = '3sangaree'
salt     = 'gAYoN3qeDKk8m2YUnleS8bHE0sYWZsxv'
concat = salt + password
print(concat)

hashed_password = hashlib.sha256(str(concat).encode('utf-8')).hexdigest()
print(hashed_password)

salt     = 'w3XSaku1XM3K6P2bL0geCZVQlxaM38VJ'
concat = salt + password
print(concat)

hashed_password = hashlib.sha256(str(concat).encode('utf-8')).hexdigest()
print(hashed_password)







        

