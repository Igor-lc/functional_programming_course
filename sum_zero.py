from functools import reduce
from sys import argv
s = list(map(int, argv[1].split()))

# ver 4
def sum_to_zero(d1, d2):
    if type(d1) == int:
        d1 = [True, d1]
    if d2 == 0:
        d1[0] = False
    if d1[0]:
        d1[1] = d1[1] + d2
    return d1

result = reduce(sum_to_zero, s)
print(result[-1])

# ver 3
i = [0, 0]
def sum_to_zero(d1, d2):
    res = d1 + d2
    if d2 == 0 and i[1] == 0:
        res -= sum(s[i[0] + 2:])
        i[1] = 1
    i[0] += 1
    return res
print(reduce(sum_to_zero, s))

# ver 1
result, q = 0, 0
def sum_to_zero(d1, d2):
    global result, q
    res = d1 + d2
    if d2 == 0 and q == 0:
        q += 1
        result = res
    result = (result, res)[d2 != 0 and q == 0]
    return res
reduce(sum_to_zero, s)
print(result)


# ver 2
r = [0, 0]
def sum_to_zero(d1, d2):
    res = d1 + d2
    if d2 == 0 and r[1] == 0:
        r[0] = res
        r[1] = 1

    r[0] = (r[0], res)[r[1] == 0 and d2 == s[len(s) - 1]]
    return res
reduce(sum_to_zero, s)
print(r[0])


