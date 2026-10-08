num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")



num1, num2,num3 = map(int, input("Enter three numbers: ").split())

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number")
elif num3 >= num1 and num3 >= num2:
    print(f"{num3} is the largest number")


def Check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if Check_leapyear(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    