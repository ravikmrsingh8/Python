from functools import reduce
# from a list get all even numbers then find sum of them

l = [1, 2, 3, 4, 5, 6, 7, 8]
print("Numbers {}".format(l))
le = list(filter(lambda e: e % 2 == 0, l))
print("All Even {}".format(le))

sum_even = reduce(lambda s, v: s + v, le)
print("Sum Even {}".format(sum_even))
