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

nums = [10, 20, 30, 40, 50]

print(sum(nums))
print(max(nums))
print(min(nums))
print(len(nums))
print(sorted(nums))
