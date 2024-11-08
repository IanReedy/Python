try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum is:", num1 + num2)
except ValueError:
    print("Please enter valid numbers.")
