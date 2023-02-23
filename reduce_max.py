from functools import reduce
from sys import argv
data = list(map(int, argv[1:]))
# ver1
new = [0]
def is_m(j):
    if j > new[-1]:
        new.append(j)
        return j
print(reduce(lambda x, y: str(x) + ', ' + str(y), list(filter(is_m, data))))

# ver2
def collect_max_values(result, value):
    if value > result[0]:
        return value, result[1] + [value]
    return result[0], result[1]

max_values = reduce(collect_max_values, data, (float("-inf"), []))
print(", ".join(map(str, max_values[1])))


# ver3 Вычисление в одну строку.
print(", ".join(map(str, reduce(lambda r, v: (v, r[1] + [v]) if v > r[0] else (r[0], r[1]), map(int, argv[1:]), (float("-inf"), []))[1])))

# ver4
def collect_max_values(result, value):
    if type(result) is not tuple:
        if value > result:
            return value, [result, value]
        return result, [result]
    if value > result[0]:
        return value, result[1] + [value]
    return result[0], result[1]

max_values = reduce(collect_max_values, data)
print(", ".join(map(str, max_values[1])))
