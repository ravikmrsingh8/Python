from collections import OrderedDict

if __name__ == "__main__":
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    d['e'] = 5
    for k,v in d.items():
        print("Key {}, value {}".format(k,v))