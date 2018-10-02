from threading import Thread


class Counter(Thread):

    def run(self):
        for x in range(1000):
            print(self.getName(), x)


if __name__ == "__main__":
    counter1 = Counter(name="Counter1")
    counter1.start()

    counter2 = Counter(name="Counter2")
    counter2.start()


