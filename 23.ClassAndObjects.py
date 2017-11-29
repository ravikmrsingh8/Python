class Sample(object):
    pass

x = Sample()
print(type(x))


class Dog(object):

    def __init__(self, breed):
        self.breed = breed


sam = Dog('Lab')
ham = Dog(breed='Huskie')

print(sam.__class__)

print(sam)
print(sam.breed)

print(ham)
print(ham.breed)


class Dog(object):
    # Class Attribute
    species = 'Mammal'

    def __init__(self, name, breed):
        self.breed = breed
        self.name = name
        self.species = 'Mammal2'

sam = Dog('Sammy', 'Lab')
print(sam.breed)
print(sam.name)
print(sam.species)

sam.species = 'Camel'
print("Sam.species {}".format(sam.species))

fam = Dog('Fammy', 'Huskie')
print(fam.species)
print(fam.name)
print(fam.breed)


class Circle(object):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius**2


print("Circle.PI {}".format(Circle.PI))

c1 = Circle(7)
print("Radius Of circle {:10.2f} and it's Area is :{:10.2f}".format(c1.radius, c1.area()))
print("Radius Of circle {:0<10.2f} and it's Area is :{:0<10.2f}".format(c1.radius, c1.area()))
print("Radius Of circle {:0>10.2f} and it's Area is :{:0>10.2f}".format(c1.radius, c1.area()))

c1.some_random_att = 7
print(c1.some_random_att)