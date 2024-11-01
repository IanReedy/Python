# This code defines a Die class that rolls a random number based on its number of sides.

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

six_sided_die = Die()
for _ in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
for _ in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
for _ in range(10):
    twenty_sided_die.roll_die()
