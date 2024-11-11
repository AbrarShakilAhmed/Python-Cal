import math

def scientific_calculator():
    print("Welcome to the Python Scientific Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log base 10)")
    print("11. Natural Logarithm (ln)")
    
    operation = input("Enter the number corresponding to the operation: ")
    
    if operation in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '5':
            result = math.pow(num1, num2)
            print(f"The result of {num1} ^ {num2} is {result}")
    
    elif operation == '6':
        num = float(input("Enter the number: "))
        if num >= 0:
            result = math.sqrt(num)
            print(f"The square root of {num} is {result}")
        else:
            print("Error: Square root of a negative number is not allowed.")
    
    elif operation == '7':
        angle = float(input("Enter the angle in degrees: "))
        result = math.sin(math.radians(angle))
        print(f"The sine of {angle} degrees is {result}")
    
    elif operation == '8':
        angle = float(input("Enter the angle in degrees: "))
        result = math.cos(math.radians(angle))
        print(f"The cosine of {angle} degrees is {result}")
    
    elif operation == '9':
        angle = float(input("Enter the angle in degrees: "))
        result = math.tan(math.radians(angle))
        print(f"The tangent of {angle} degrees is {result}")
    
    elif operation == '10':
        num = float(input("Enter the number: "))
        if num > 0:
            result = math.log10(num)
            print(f"The logarithm (base 10) of {num} is {result}")
        else:
            print("Error: Logarithm of zero or a negative number is not defined.")
    
    elif operation == '11':
        num = float(input("Enter the number: "))
        if num > 0:
            result = math.log(num)
            print(f"The natural logarithm of {num} is {result}")
        else:
            print("Error: Natural logarithm of zero or a negative number is not defined.")
    
    else:
        print("Invalid input. Please choose a valid operation.")

scientific_calculator()
