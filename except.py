# **************************************************
# Author - Harshit Prasad
# 18.12.2016
# Python program - Introduction to try and except
# ***************************************************

while True:
    try:
        number = int(input("Enter a number - \n"))
        print(18/number)
        break
    except ValueError:
        print('Please enter a number not a character!')
    except ZeroDivisionError:
        print('Do not enter number 0')

