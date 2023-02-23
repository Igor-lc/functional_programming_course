l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_square = []


def square(x):
    return x ** 2


def is_even(j):
    return j % 2 == 0


for i in l:
    l_square.append(square(i))

l_square_2 = list(map(square, l))
l_square_3 = list(map(str, filter(is_even, l)))


print(l_square)
print(l_square_2)
print(l_square_3)
