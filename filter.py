l = [4, 17, 23, 12, 6, 57, 84]
l2 = []

def is_even(j):
    return j % 2 == 0

def gt_10(j):
    return j > 10

for i in l:
    if is_even(i) and gt_10(i):
        l2.append(i)

l3 = list(filter(gt_10, filter(is_even, l)))
print(l2)
print(l3)
