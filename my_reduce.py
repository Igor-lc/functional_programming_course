
import time
start = time.time()

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']
l = range(1, 6)

def mult(x, y):
    return x * y

def concat(x, y):
    return x + y

def myreduce(func, sequence):
    new = None
    for i, j in enumerate(sequence[:-1]):
        if i == 0:
            new = func(sequence[i], sequence[i+1])
        else:
            new = func(new, sequence[i+1])
    return new

def myreduce2(func, seq):
    result = func(seq[0], seq[1])
    for el in seq[2:]:
        result = func(result, el)

    return result

print(myreduce(concat, whoami))
print(myreduce2(mult, l))

print(time.time() - start)
