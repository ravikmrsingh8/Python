import statistics as stats


def getMean(marks):
    print(stats.mean(marks))


if __name__ == "__main__":
    marks = [10, 34, 56, 12, 34, 41, 40]
    getMean(marks)

