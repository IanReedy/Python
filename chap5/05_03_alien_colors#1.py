"""
I assign the string 'green' to the variable `alien_color` and check if it equals 'green'. 
Since the condition is true, I print a message indicating that 5 points have been earned. 
I then assign the string 'yellow' to `alien_color2` and check if it equals 'green', but since this condition is false, no message is printed.
"""

alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')

alien_color2 = 'yellow'
if alien_color2 == 'green':
    print('You just earned 5 points!')
