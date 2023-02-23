from functools import reduce
import re
import sys
char = "  " + sys.argv[1]

# ver 1
char = sys.argv[1]
print(re.sub(r'(\w+)(\s{1})([!.?])', r'\1\3', char))


# ver 2
def mess(text, char):
    if char in '.!?':
        if text[-1] == ' ' and text[-2] != ' ':
            return text[:-1] + char
    return text + char
print(reduce(mess, char))
