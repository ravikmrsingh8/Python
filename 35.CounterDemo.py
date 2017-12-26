from collections import Counter


def findMostNCommonLetters(sentence, N):
    return Counter(sentence).most_common(N)


def findMostNCommonWords(sentence, N):
    return Counter(list(map(lambda s: s.strip(), sentence.split()))).most_common(N)

def findLettersCountAsDict(sentence):
    return dict(Counter(sentence))

def printMostCommon(c):
    for item, count in c:
        print("Item :'{}', Count: {}".format(item, count))


if __name__ == "__main__":
    sentence = "Do you understand list comprehensions? If so, a generator expression is like a list comprehension, but instead of finding all the items you're interested and packing them into list, it waits, and yields each item out of the expression, one by one."
    c = findMostNCommonLetters(sentence, 3)
    print("\nMost Common 3 Letters")
    printMostCommon(c)
    c = findMostNCommonWords(sentence, 3)
    print("\nMost Common 3 Words")
    printMostCommon(c)

    lettersCount = findLettersCountAsDict(sentence)
    for key,value in lettersCount.items():
        print("Item '{}', Count{}".format(key,value))



