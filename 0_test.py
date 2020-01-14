def getLetterList(words):
    letter_set = set()
    for word in words:
        for letter in word:
            letter_set.add(letter)
    return list(letter_set)


def initLetterOrderList(letter_set):
    lessOrderMap = {}
    largerOrderMap = {}
    for letter in letter_set:
        lessOrderMap[letter] = set()
        largerOrderMap[letter] = set()
    return lessOrderMap, largerOrderMap


def compareWord(s1, s2):
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return s1[i], s2[i]
    return None


# print(compareWord('abc', 'abcz'))
# print(compareWord('abc', 'abz'))
# print(compareWord('xabc', 'yabz'))
letter_set =[
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]
print(initLetterOrderList(getLetterList(letter_set)))
