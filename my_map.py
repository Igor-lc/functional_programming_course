numbers1 = [1, 2, 3]
numbers2 = [4, 5]


def mymap(funk, *args):
    res = []
    for i in range(len(min(args, key=len))):
        print(args[i][i])
        res.append(funk[args[i][i]] + funk[args][i][i])
        return res

result = mymap(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
