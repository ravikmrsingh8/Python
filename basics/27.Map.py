
l = [0, 37, 45, 100, 120]
# convert temperatures into fahrenheit
f = list(map(lambda t: (9/5) * t + 32, l))
print("Temperature in Fahrenheit {}".format(f))

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

aggregator = list(map(lambda x, y, z : x + y +z, l1, l2, l3))
print("Aggregator: {}".format(aggregator))


