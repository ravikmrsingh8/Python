from numpy import random
import numpy as np
import matplotlib.pyplot as plt


def sinplot():
    x = np.linspace(0, 14, 100)
    plt.plot(x, np.sin(x))
    plt.ylabel("sin(x)")
    plt.xlabel("x")
    plt.show()


def run():
    print(np.zeros(10))
    print(np.arange(10, 21))
    print(np.arange(0, 9).reshape(3, 3))
    print(np.identity(3))
    print(random.rand())
    a = np.arange(0, 16).reshape(4, 4)

    print(a)
    print("")
    print(a[1:][1:])
    np.random.seed(sum(map(ord, "aesthetics")))
    sinplot()


if __name__ == "__main__":
    run()
