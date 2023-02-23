from functools import reduce

def normalize_phone(ph):
    return reduce(lambda x, y: x + y, (filter(lambda i: i.isdigit(), ph)))

phone = normalize_phone("+1 (669) 452-79-72")
print(phone)



def normalize_phone2(x):
    return ''.join(filter(lambda x: x.isdigit(), x))

print(normalize_phone2("+1 (669) 452-79-72"))




def normalize_phone3(number):
    return ''.join([i for i in number if i.isdigit()])
print(normalize_phone3("+1 (669) 452-79-72"))



def normalize_phone4(number):
    return "".join(filter(str.isdigit, phone))
print(normalize_phone4("+1 (669) 452-79-72"))
