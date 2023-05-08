def mymap(funk, *args):
    res = []
    for i in zip(*args):
        res.append(funk(*i))
    return res


def maps(*funks):
    ress = funks[-1]
    for i in (funks[:-1]):
        ress = mymap(i, ress)
    return ress


print(maps(str.strip, str.lower, [" python", "SQL", " PHP "]))  # ["python", "sql", "php"]


'''MAPS
Difficulty: 6 out of 10
The original map only allows one function to be applied to the elements of a sequence. However, it is often necessary to apply several maps in a row at once.

Write a maps function that can take multiple functions. The functions must be applied to the sequence in the order in which they appear. The last argument must be the sequence itself.

Usage example
original_tags = ["python", "SQL", "PHP"]
tags = maps(str.strip, str.lower, original_tags)
# After executing the code, the tags variable will contain the list ["python", "sql", "php"]'''
