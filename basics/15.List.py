def list_demo():
    letters = ['A', 'B', 'C', 'D']
    print(letters)
    print(letters[1])

    # list comprehension
    numbers = [2, 1, 4, 3, 5]
    squared_list = [x ** x for x in numbers]
    print(squared_list)

    even_num = [x for x in range(21) if x % 2 == 0]
    print(even_num)

    # list methods
    numbers.sort()
    print(numbers)


if __name__ == "__main__":
    list_demo()
