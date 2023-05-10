from sys import argv
from functools import reduce
from itertools import accumulate
revenue = list(map(int, argv[1:]))
print(revenue)

# ver 1
result = reduce(lambda x, y: x + [x[-1] + int(y)], revenue[1:], [revenue[0]])
print(*result)

# ver 2
print(*list(accumulate(revenue)))
