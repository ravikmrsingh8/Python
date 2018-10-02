import matplotlib.pyplot as plt


def plotNumberVsIndex():
    plt.plot([1,1,2,2,3,3,4])
    plt.ylabel("some numbers")
    plt.xlabel("index")
    plt.show()


def plotIcecreamVsTemp(a,b):
    plt.plot(a, b)
    #plot.ylabel("Ice Cream Sales")
    #plot.xlabel("Temperature")
    plt.show()


if __name__ == "__main__":
    #plotNumberVsIndex()
    plotIcecreamVsTemp([35,20,40],[400,200,500])
    #plot.plot([1,2,3,4],[1,4,9,16])
    #plot.show()

