# ************************************************************
# Author - Harshit Prasad
# 18.12.2016
# Python Program - Classes and Objects.
# ************************************************************

class Enemy:
    life = 3 # defining a variable in a class.
    def attack(self):
        print('ouch!')
        self.life -= 1

    def checklife(self):
        if self.life <=0:
            print("'You're dead!")
        else:
            print(self.life, 'life left.')

enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.attack()
# enemy 1 has been attacked two times.
enemy2.checklife()
enemy1.checklife()
# Here since enemy2 is not attacked, his life will be equal to 3.
# Whereas, enemy1 has been attacked 2 times. So, his life will become 1.