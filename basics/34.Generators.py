import random


def genSquares(n):
    for x in range(n):
        yield x**2


def genRandom(min,max,count):
    for i in range(count):
        yield random.randint(min,max)

def genComprehension():
    return (item for item in range(1000000000000))

if __name__ == "__main__":
    print("Squares: ")
    for i in genSquares(10):
        print(i, end=",")

    print("\nRandom: ")
    for i in genRandom(1,10,10):
        print(i, end=",")

    print("\nGenerator Comprehension :")
    genComp = genComprehension()
    print(next(genComp))
    print(next(genComp))
    print(next(genComp))
    print(next(genComp))

