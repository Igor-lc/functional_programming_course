from functools import reduce
import time
start_time = time.time()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(j):
    return j % 2 == 0

def my_filter(filter_func, values):
    new_values = []
    for value in values:
        if filter_func(value):
            new_values.append(value)
    return new_values

#print(my_filter(is_even, l))
#print("--- %s seconds ---" % (time.time() - start_time))



def square(x):
    return x ** 2

def my_map(map_func, values):
    new_values = []
    for value in values:
        new_values.append(map_func(value))
    return new_values

#print(my_map(square, l))


