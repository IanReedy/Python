# This code simulates a lottery by randomly selecting 4 characters from a set list.

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_pool, 4)
print("Any ticket matching these numbers or letters wins a prize:", winning_numbers)
