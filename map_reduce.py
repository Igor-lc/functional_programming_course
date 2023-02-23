from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]


def s(r):
    return r["length"] * r["width"]


def sum_(x, y):
    return x + y


rooms = list(map(s, rooms))
square = reduce(sum_, rooms)
print(square)
