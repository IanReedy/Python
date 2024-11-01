# This code runs a loop that keeps pulling random numbers until a specified ticket wins, reporting attempts.

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = [1, 'A', 4, 'D']
attempts = 0

while True:
    attempts += 1
    drawn_ticket = random.sample(lottery_pool, 4)
    if set(drawn_ticket) == set(my_ticket):
        print("Winning ticket:", drawn_ticket)
        print("Number of attempts to win:", attempts)
        break
