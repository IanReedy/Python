"""
I assign the string 'green' to the variable `alien_color` and check if it equals 'green'. 
Since the condition is true, I print a message indicating that 5 points have been earned. 
Next, I assign the string 'red' to `alien_color` and again check if it equals 'green'. 
Since this condition is false, I print a message indicating that 10 points have been earned.
"""

alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')
elif not alien_color == 'green':
    print("You just earned 10 points")

alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points!')
elif not alien_color == 'green':
    print("You just earned 10 points!")