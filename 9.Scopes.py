# A variable which is defined in the main body of a file is called a global variable.
# It will be visible throughout the file, and also inside any file which imports that file.

x = 10


def scope_test():
    # A variable which is defined inside a function is local to that function.
    # It is accessible from the point at which it is defined until the end of the function
    z = 7

    print(z)
    print(x)
    # x = x + 1 (Not Allowed. Why?)

a = 10


def change_global():
    global a
    a = 20

# c = 30
# def test():
#     print(c)
#     c = 30
#     print(c)

scope_test()
print("X = ", x)
print("a =", a)
change_global()
print("a =", a)
# test()
# print(c)
# print(globals())
