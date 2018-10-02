import sys

num1 = 6
print("size of {} is {}".format(num1, sys.getsizeof(num1)))


# 25 bytes is reserved for string then it will grow by  1 byte for each character
ch = 'h'
print("size of {} is {}".format(ch, sys.getsizeof(ch)))


ch = 'ch'
print("size of {} is {}".format(ch, sys.getsizeof(ch)))

greet = "Hello World!"   # 12 Characters
print("size of {} is {}".format(greet, sys.getsizeof(greet)))

# print = print(56) you shouldn't do this

a = None
print(a)
print("size of {} is {} ".format(a, sys.getsizeof(a)))
