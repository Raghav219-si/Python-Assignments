# *****************
# Author - Harshit Prasad
# 17.12.2016
# Program to determine odd and even number
# *****************
def check(n):
    if n % 2 == 0:
        print(n, "is even.")
    else:
        print(n, "is odd.")

number = int(input("Please enter a number - \n"))
if number < 0:
    print("Please enter a valid number!")
else:
    check(number)

