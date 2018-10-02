def foo():
    pass


class A(object):
    pass


def type_of_test():
    name = "bucky"
    print(type(name))

    marks = 100
    print(type(marks))

    ch = 'h'
    print(type(ch))

    sal = 3.4
    print(type(sal))

    l1 = list()
    print(type(l1))
    print(range(9))

    print(type(list(range(10))))

    print(type(foo))

    an_object = A()
    print(type(an_object))


if __name__ == "__main__":
    type_of_test()

