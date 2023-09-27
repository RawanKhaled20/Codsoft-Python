""" Author: Rawan Khaled https://github.com/RawanKhaled20/Codsoft-Python.git"""

#Addtion operation
def add(x, y):
    return x + y
#Subtraction operation
def subtract(x, y):
    return x - y
#Multiplication operation
def multiply(x, y):
    return x * y
#Division operation
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
#Modulus/Remiander operation
def modulus(x, y):
    return x%y
#Exponential opertaion
def exponential(x, y):
    return x**y

if __name__ == '__main__':
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponent")

    operation =int(input("Enter operation number (1/2/3/4/5/6): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif operation == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == 3:
        print(num1, "X", num2, "=", multiply(num1, num2))
    elif operation == 4:
        print(num1, "/", num2, "=", divide(num1, num2))
    elif operation == 5:
        print(num1, "%", num2, "=", modulus(num1, num2))
    elif operation == 6:
        print(num1, "^", num2, "=", exponential(num1, num2))
    else:
        print("Invalid operation")


