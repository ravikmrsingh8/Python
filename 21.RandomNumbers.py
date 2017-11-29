import random

rand_number = random.randint(0, 99)
print(rand_number)

l = [0, 1, 3, 4, 5, 6, 7, 2, 7, 8]

print("List :" + str(l))
random.shuffle(l)
print("shuffled List " + str(l))

count = 0
while True:
    rand_number = random.choice(l)
    print(rand_number, end=" ")
    count += 1
    if count > 8:
        break
