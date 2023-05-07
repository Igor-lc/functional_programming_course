numbers1 = [1, 2, 3, 2]
numbers2 = [4, 5, 6]


def mymap(funk, *args):
    res = []
    for i in zip(*args):
        res.append(funk(*i))
    return res



print(list(mymap(lambda x, y: x + y, numbers1, numbers2)))
