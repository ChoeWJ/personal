numbers = [1, 2, 3, 4, 5]

# origin
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)

# comprehension
squared = [num ** 2 for num in numbers]
print(squared)

# if
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# if-else
labels = ['짝수' if num % 2 == 0 else "홀수" for num in numbers]
print(labels)

# 중첩
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)

# dictionary
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)

# enumerate
names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names, start=1):
    print(i, name)
    
# enumerate comprehension
result = [print(i, name) for i, name in enumerate(names, start=1)]

# save list
result = [(i, name) for i, name in enumerate(names, start=1)]
print(result)



