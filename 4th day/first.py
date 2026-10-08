"""

fru = ["apple", "banana", "cherry"]
num = [1, 2, 3, 4, 5]
mix = [1, "hello", 3.14, True]

empty_list = []

print(fru)
print(num)
print(mix)
print(empty_list)

print(num[2])
print(mix[1])
print(fru[-1])

"""
"""
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
print(nums[:3])
print(nums[2:])
print(nums[-3:-1])
print(nums[::2])



fru = ["apple", "banana", "cherry"]

fru[0] = "kiwi"
fru.append("orange")
fru.insert(1, "mango")
fru.extend(["grape", "pear"])
print(fru)

"""
"""
iteam = [1, 2, 3, 4, 5]
iteam.remove(3)
iteam.pop()
iteam.pop(1)
print(iteam)

del iteam[0]
print(iteam)

"""
"""
marks = [90, 80, 70, 60, 50]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()

print(33 in marks)
print(marks.count(70))
print(marks.index(60))
"""
"""
names = ["ommii","Prathiksha", "sakshi", "samarth"]

for name in names:
    print(name)

for i , name in enumerate(names):
    print(i, name)



"""
"""
nums = [10, 20, 30, 40, 50]

print(sum(nums))
print(max(nums))
print(min(nums))
print(len(nums))
print(sorted(nums))

squares = [x**2 for x in range(1, 6)]
print(squares)

even_nums = [x for x in range(1, 11) if x % 2 == 0]
print(even_nums)

"""
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][1])
print(matrix[1][2])

"""
"""
point = (3, 4)
colours = ("red", "green", "blue")


print(point[0])
print(colours[1])


a = (5)
b = (5,)

print(type(a))
print(type(b))
"""
"""
student = ("Omii", 20, "Pune")

name, age, city = student
print(name)
print(age)
print(city)

"""
"""
t = (1, 2, 3, 4, 5)

print(t.count(3))
print(t.index(4))
"""
"""
student = {
    "name": "Omii",
    "age": 20,
    "city": "Pune"

}

print(student["name"])
print(student.get("age"))

print(student.get("age"))
print(student.get("name"))
print(student.get("phone", "NA"))

student["course"] = "Python"
student["age"] = 21
student.update({"city": "Mumbai"})

student.pop("course")
del student["age"]

print(student.keys())



d = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

"""
"""
marks = {
    "math": 90,
    "science": 80,
    "english": 70
}


for subject, mark in marks.items():
    print(f"{subject}: {mark}")


word_list = ["ai", "py", "ml", "ds"]
count = {}

for w in word_list:
    count[w] = count.get(w, 0) + 1

print(count)


"""

students = {
    "a" : {"name": "omiii", "marks": 90},
    "b" : {"name": "pratiksha", "marks": 80}
}

print(students["a"]["name"])


nums = {1, 2, 2, 3, 4, 4, 5}
print(nums)

empty = set()

