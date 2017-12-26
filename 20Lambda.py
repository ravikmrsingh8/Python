square = lambda x: x**2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(square(2))
l = [square(x) for x in numbers]
print("list :{}".format(l))

ll = list(map(square, numbers))
print("After Mapping {}".format(ll))

print("Original List :{}".format(numbers))


def test():
    print("From lambda")

def invoke(iterable, func):
    for item in iterable:
        print(func(item), end=" ")


print()
invoke([1, 2, 3], lambda x: x**2)

print()
invoke([1, 2, 3], lambda x: x**3)

print()
invoke([1, 2, 3], lambda x: x+1)

print()
invoke([1, 2, 3], lambda x: 1/x)
