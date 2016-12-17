# ******************
# Author - Harshit Prasad
# 17.12.2016
# Python program which checks about a number less than 10
# ******************

# list of numbers
number[10] = [1, 3, 5, 6, 7, 9, 10, -1, 2, -2]

def usercheck():
    for numbers in range(0,9):
        if number[numbers] > user:
            print(str(number[numbers]))

for i in range(0,9):
    if number[i] > 5:
        print(number[i])

user = int(input("Enter a number - ")) # The list of numbers you want greater than the number you have typed
if user < 0:
    print("Please enter a positive number!")
else:
    usercheck(user)