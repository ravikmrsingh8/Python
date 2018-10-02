# use zip to make pair from elements of two list them print pair whose sum is greatest among all

# (12, 10), (1, 3)
def get_max_sum_pair(l1, l2):
    sum = 0
    for pair in zip(l1, l2):
        x, y = pair
        sum = max(sum, x+y)
    return sum

l1 = [12, 1, 3, 5, 9, 10]
l2 = [10, 3, 12, 9, 10, 20]
print(get_max_sum_pair(l1, l2))
