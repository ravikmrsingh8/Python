greet = str("Hello World!")
print(greet)
print("length of {} is {}".format(greet, len(greet)))

# Indexing
print(greet[0])
print(greet[-1])
print(greet[-4])
# greet[-20], greet[20] will through index error
# slicing
print(greet[0:10])
print(greet[:10])
print(greet[:])
print(greet[2:])

# stepping
print(greet[0:10:2])
print(greet[::1])
print(greet[::-1])


# String concatenation
print(greet + "You don't have any idea what could be appended to you!, Do You?")
print(greet * 3)

print(greet.upper())

# String immutability
# greet[0] = 'K'   # Not Allowed
