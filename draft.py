numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7, 9] 1 + 4, 2 + 5, 3 + 6
