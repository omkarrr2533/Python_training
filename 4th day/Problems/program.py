num = [10, 20, 30, 40, 50]

print(sum(num))
print(max(num))
print(min(num))
print(sum(num)/ len(num))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [num for num in numbers if num % 2 == 0]

print(evens)




print(numbers[::-1])
numbers.reverse()
print(numbers.reverse)

reversed_list = []

for item in numbers:
    reversed_list.insert(0, item)

print(numbers)



nums = [10,20,10,30,40,50,10,10]
nums = set(nums)
nums = list(nums)
print(nums)


temp = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = temp

print(numbers)



stu = {
    "om": "95",
    "Sujal": "90",
    "Pratiksha": "45"
}


