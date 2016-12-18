# ************************************************
# Author - Harshit Prasad
# 19.12.2016
# Python program - Introduction to function init.
# ************************************************

class Enemy:
    def __init__(self, x):
        self.energy = x # Storing energy in a variable-name 'energy'

    def get_energy(self):
        print(self.energy)

harshit = Enemy(100)
vaibhav = Enemy(50)

harshit.get_energy()
vaibhav.get_energy()
