numbers1 = [1, 2, 3, 2]
numbers2 = [" python", "SQL", " PHP "]


def mymap(func, *seq):
    newseq = []

    # Ищем размер минимальной последовательности
    min_list_len = min([len(s) for s in seq])

    # Теперь идем по элементам последовательностей
    for i in range(min_list_len):
        # Формируем аргументы функции из элементов последовательностей
        func_args = []
        for s in seq:
            func_args.append(s[i])

        # Раскрываем fun_args и вставляем в функцию
        newseq.append(func(*func_args))

    return newseq


def mymap2(funk, *args):
    newseq = []
    for i in zip(*args):
        newseq.append(funk(*i))
    return newseq


print(list(mymap(str.lower, numbers2)))
print(list(mymap2(str.lower, numbers2)))



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
