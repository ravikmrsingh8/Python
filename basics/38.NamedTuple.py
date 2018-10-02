from collections import namedtuple

if __name__ == "__main__":
    Dog = namedtuple("Dog", "fur name claws")
    d1 = Dog(fur=True, name="Sam", claws=False)
    print(d1)

    Cat = namedtuple("Cat", "fur name grumpy")
    c1 = Cat(fur=True, name="Kitty", grumpy=False)
    print(c1)
