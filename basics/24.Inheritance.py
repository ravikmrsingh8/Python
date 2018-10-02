class Animal(object):
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("Dog")

d = Dog()
d.who_am_i()
d.eat()