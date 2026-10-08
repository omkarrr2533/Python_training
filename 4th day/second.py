with open("notes.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("file handling is easy\n")


with open("notes.txt", "r") as f:
    content = f.read()

print(content)



with open("notes.txt") as f:
    for line in f:
        print(line.strip())

with open("notes.txt") as f:
    lines = f.readlines()

print(len(lines))


with open("notes.txt","a") as f:
    f.write("A new line\n")

try:
    with open("data.txt") as f:
        print(f.read())

except FileNotFoundError:
    print("file not found")



names = ["Riya", "Aman", "Omii"]

with open("names.txt",  "w") as f:
    for n in names:
        f.write(n + "\n")