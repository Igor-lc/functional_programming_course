import time as t
start_time = t.time()
print(start_time)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(j):
    return j % 2 == 0


print(list(filter(is_even, l)))
print(t.time() - start_time)
