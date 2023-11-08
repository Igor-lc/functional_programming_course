from sys import argv
word = argv[1]


def first(i):
    if i == 0:
        print(word[i], end=' ')


def last(i):
    if i == len(word) - 1:
        print(word[i])

''.join(map(str, filter(first, [i for i, w in enumerate(word)])))
''.join(map(str, filter(last, [i for i, w in enumerate(word)])))