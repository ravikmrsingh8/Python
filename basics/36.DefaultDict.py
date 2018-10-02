from collections import defaultdict

# default dict will never raise key error it will create one and put the default value
def run():
    d = defaultdict(lambda: 0)
    print(d['one'])
    print(d)
    print(d['two'])
    print(d)
    d['three'] = 3
    print(d)


if __name__ == "__main__":
    run()