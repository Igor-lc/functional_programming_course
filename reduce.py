from functools import reduce
l = range(1, 6)
def mult(x, y):
    return x * y
print(reduce(mult, l))


gamers = [
    {"name": "Alexandr", "goals": 7, "pass": 5},
    {"name": "Oleg", "goals": 6, "pass": 4},
    {"name": "Pavel", "goals": 8, "pass": 10},
    {"name": "Halk", "goals": 13, "pass": 14}
]

def goal_pass(gamer):
    return {"name": gamer["name"], "gp": gamer["goals"] + gamer["pass"]}
print(list(map(goal_pass, gamers)))

def best_gamer(gamer1, gamer2):
    if gamer1["gp"] > gamer2["gp"]:
        return gamer1
    return gamer2

print(reduce(best_gamer, map(goal_pass, gamers)))


whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']
def concat(x, y):
    who_am_i = x + y
    return who_am_i

print(reduce(concat, whoami))
