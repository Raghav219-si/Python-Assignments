# ********************************************************************************
# Author - Harshit Prasad
# 19.12.2016
# Python program : to reverse a string and check whether it's a palindrome or not.
# *********************************************************************************

# We will use - inbuilt functions like reversed() - which reverse each alphabet
# list() - which create the list of alphabets.
name = input('Enter your name!')
rev_name = reversed(name)
if list(name)==list(rev_name):
    print('It is a palindrome.')

else:
    print('It is not a palindrome.')

# It is for lower case letters only.

# Extras
# We can also write it as -
new_name = input('Enter your new name -')
if new_name == new_name[::-1]: # applicable for lower case letters only
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')

# Extras again.
extra = 'Hello, My name is Python.'
len_of_extra = len(extra)
print(len_of_extra)

words = extra.count('name')
print(words)