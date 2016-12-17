# Author - Harshit Prasad
# 18.12.2016
# Python program which calculates the factorial of a number

def factorial(n): # Here we will be going to use recursion method
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number = int(input("Enter the number of which factorial is to be calculated-"))
if number == 0:
    print("Factorial of 0 is 1.")
elif number < 0:
    print("Factorial of a negative number does not exist.")
else:
    print("Factorial of the", number, "is", factorial(number))
