letters = ['A', 'B', 'C', 'D']
print(letters)

# list comprehension
numbers = [2, 1, 4, 3, 5]
squared_list = [x ** x for x in numbers]
print(squared_list)

even_num = [x for x in range(21) if x % 2 == 0]
print(even_num)



# list methods
numbers.sort()
print(numbers)