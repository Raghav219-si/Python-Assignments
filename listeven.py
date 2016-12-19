# ***************************************************
# Author - Harshit Prasad
# 19.12.2016
# Python program - Creating a list of random numbers, and then creating other new list in which, even numbers are stored.
# ***************************************************
import random
a = [random.randrange(1,20) for x in range(10)]
print (a)

new_a = []
for numbers in a:
    if numbers % 2 == 0:
        new_a.append(numbers)

print(new_a)
