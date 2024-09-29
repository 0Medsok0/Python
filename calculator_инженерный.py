import math

def engineering_calculator():
    print("Welcome to the Engineering Calculator!")
    print("Operations: +, -, *, /, sin, cos, tan, log, exp")

    while True:
        operation = input("Enter operation: ")

        if operation in ['+', '-', '*', '/']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                print(num1 + num2)
            elif operation == '-':
                print(num1 - num2)
            elif operation == '*':
                print(num1 * num2)
            elif operation == '/':
                if num2 != 0:
                    print(num1 / num2)
                else:
                    print("Error! Division by zero is not allowed.")

        elif operation in ['sin', 'cos', 'tan']:
            num = float(input("Enter number: "))

            if operation == 'sin':
                print(math.sin(num))
            elif operation == 'cos':
                print(math.cos(num))
            elif operation == 'tan':
                print(math.tan(num))

        elif operation == 'log':
            num = float(input("Enter number: "))
            if num > 0:
                print(math.log(num))
            else:
                print("Error! Logarithm is not defined for non-positive numbers.")

        elif operation == 'exp':
            num = float(input("Enter number: "))
            print(math.exp(num))

        else:
            print("Invalid operation!")

        continue_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if continue_calculation.lower() != 'yes':
            break

    print("Thank you for using the Engineering Calculator!")

engineering_calculator()