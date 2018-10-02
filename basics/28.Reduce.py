from functools import reduce

# idea is to convert temperature into fahrenheit and then find max temp
tc = [0, 20, 37, 45, 100]
print("Temperature in *C {}".format(tc))

tf = list(map(lambda t: (9/5)*t + 32, tc))
print("Temperature in *F {}".format(tf))

max_tf = reduce(lambda t1, t2: t1 if t1 > t2 else t2, tf)
print("Maximum Temp {}".format(max_tf))
