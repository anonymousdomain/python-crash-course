from random import randint
class Dice:
    def __init__(self):
        self.sides=6
    def rolldie(self):
        sides=randint(1,self.sides)
        print(f"the sides we got is:{sides}")
d=Dice()
d.rolldie()
