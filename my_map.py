numbers1 = [1, 2, 3, 2]
numbers2 = [" python", "SQL", " PHP "]


def mymap(funk, *args):
    res = []
    for i in zip(*args):
        res.append(funk(*i))
    return res


print(list(mymap(str.lower, numbers2)))



'''Create a function mymap that will work just like the original map but return a list.

Keep in mind that map can accept multiple sequences at once.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7, 9] 1 + 4, 2 + 5, 3 + 6
If the sequences have different lengths, then the shortest one will be taken as the main one.

numbers1 = [1, 2, 3]
numbers2 = [4, 5]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7] 1 + 4, 2 + 5'''
