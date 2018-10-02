from functools import reduce


def word_length(phrase):
    return list(map(lambda s: len(s), phrase.split()))


len_word_list = word_length("Hello, How are You?")
print(len_word_list)


def digits_to_num(digits):
    return reduce(lambda d1, d2: d1 * 10 + d2, digits)


num = digits_to_num([1, 2, 3, 4])
print(type(num))
print(num)


def filter_words(words, letter):
    return list(filter(lambda w: w[0] == letter, words))


words = ["hello", "hi", "are", "cat", "dog", "ham", "go", "to", "heart"]
print(filter_words(words, 'h'))


def concatenate(L1, L2, connector):
    return ["{}{}{}".format(x, connector, y) for x, y in zip(L1, L2)]


print(concatenate(['A', 'B'], ['a', 'b'], '-'))


def d_list(L):
    d = dict()
    for val, key in enumerate(L):
        d[key] = val
    return d

def d_list_solution(L):
    return {key:value for value,key in enumerate(L)}


print(d_list(['a', 'b', 'c']))
print(d_list_solution(['a', 'b', 'c']))


def count_match_index(L):
    result = 0
    for count, item in enumerate(L):
        result += 1 if count == item else 0
    return result

def count_match_index_solution(L):
    return len([x for i,x in enumerate(L) if i == x ])



L = [0, 2, 2, 1, 5, 5, 6, 10]
print(count_match_index(L))
print(count_match_index_solution(L))
