# *******************************************************
# Author - Harshit Prasad
# 19.12.2016
# Python program to make common list, without any occurring of duplicates.
# *******************************************************
# Extras.
list_of_students = ['Michael', 'John', 'Max']
name = input('Check the name of the student : ')
if name in list_of_students:
    print('This student is enrolled.')
# *****************************************************
import random

# Generating random numbers in list A and list B
a = [random.randrange(1,20) for i in range(10)]
b = [random.randrange(1,20) for j in range(10)]
print(a, b, '\n')

# Comparing two lists and making a new list X
new_list = [x for x in set(a+b) if x in a and x in b]
print(new_list)

