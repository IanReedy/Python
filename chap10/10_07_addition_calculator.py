while True:
    try:
        num1 = int(input("Enter the first number (or type 'quit' to exit): "))
        num2 = int(input("Enter the second number: "))
        print("The sum is:", num1 + num2)
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        break
