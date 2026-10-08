def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


a, b = int(input("Enter two numbers: ")), int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)
else:
    result = "Invalid operation"

print("Result:", result)

