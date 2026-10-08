"""userr = input("Enter your username:")
user = "Omiii"
pw = "Omii2533"


if userr == user:
    password = input("Enter your password:")
    if password == pw:
        print("Login successful")
    else:
        print("Incorrect password")

else:
    print("Incorrect username")

    

age = int(input("Enter your age: "))
status = "adult" if age >= 18 else "minor"
print(f"You are a {status}.")

name = ""
 
if name:
    print("Name is not empty")
else:
    print("Name is empty")
     

for i in range(5):
    print(i)


for ch in "AI":
    print(ch)

total = 0

for n in range(1, 11):
    total += n

print("The sum of numbers from 1 to 10 is:", total)
    

a = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{a} x {i} = {a * i} = {(a * i) * (a * i)}")

    """
"""
count = 1

while count <= 3:
    print("Count:", count)
    count += 1


    """
"""
for i in range(5, 0, -1):
    print("*" * i)


for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
    """
"""
def greet(name):
    print(f"Hello, {name}! Welcome to the program.")

greet("omiii")
greet("omkar")

    """
"""
def add(a,b):
    return a + b

result = add(5, 3)
print("The sum is:", result)
    """
"""
def Power(base, exponent):
    return base ** exponent

print(Power(2, 3))  
print(Power(5, 2))


def intro(name, city):
    print(f"My name is {name} and I live in {city}.")

intro("Omkar", "Pune")
    """
"""
def min_max(a, b):
    return min(a, b), max(a, b)

low , high = min_max(10, 20)
print("Minimum:", low)
print("Maximum:", high)


x = 10

def show():

    y = 20
    print("Inside function:", x, y)

show()
print("Outside function:", x)

    """
"""
def is_even(num):
    return num % 2 == 0

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

is_even_result = is_even(4)
factorial_result = factorial(5)
print("Is 4 even?", is_even_result)
print("Factorial of 5:", factorial_result)
"""
square = lambda x: x * x
print(square(6))