rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]


def square(y):
    for i in range(rooms.__len__()):
        rooms[i]["square"] = rooms[i]["length"] * rooms[i]["width"]
    return(y)

print(list(map(square, rooms)))


def square(y):
    return {"name": y["name"], "length": y["length"], "width": y["width"], "square": y["length"] * y["width"]}

print(list(map(square, rooms)))
