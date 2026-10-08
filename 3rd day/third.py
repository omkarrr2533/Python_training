id = input("Enter u have id or not type yes and no: ")
age = int(input("Enter your age: "))

if age >= 18 and id == "yes":
    print("You can drive")
elif age >= 18 and id == "no":
    print("You cannot drive")
elif age < 18 and id == "yes":
    print("You cannot drive")
else:
    print("You cannot drive")
