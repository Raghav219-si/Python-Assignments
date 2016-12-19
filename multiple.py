# ************************************************
# Multiple Inheritance
# Author - Harshit Prasad
# 19.12.2016

class Mario():
    def move(self):
        print('I move yo!')

class Shroom():
    def eat_shroom(self):
        print('I am growing.')

class BigMario(Mario, Shroom):
    pass # It will act as a place holder without giving any IndentationError

man = BigMario()
man.move()
man.eat_shroom()