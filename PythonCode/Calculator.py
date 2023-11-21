import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number!"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero!"

def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error: Floor division by zero!"

print("Calculator Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Square Root")
print("7. Modulus")
print("8. Floor Division")

choice = int(input("Enter operation number (1-8): "))

if choice in range(1, 9):
    if choice in [1, 2, 3, 4, 5, 7, 8]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice == 6:
        num1 = float(input("Enter number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    elif choice == 5:
        print("Result:", exponentiate(num1, num2))
    elif choice == 6:
        print("Result:", square_root(num1))
    elif choice == 7:
        print("Result:", modulus(num1, num2))
    elif choice == 8:
        print("Result:", floor_divide(num1, num2))
else:
    print("Invalid choice! Please select a number between 1 and 8.")
