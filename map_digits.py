# В списке digits содержатся строки с числами. Эти строки содержат ошибки: лишние пробелы, а также неправильные разделители целой и десятичной части.
# Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в вещественное число. Примените эту функцию ко всем элементам digits с помощью map.

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]


'''def conv(x):
    digits = [i.strip().replace(",", ".").replace(" ", "") for i in x]
    digits = [float(i) for i in digits]
    return digits'''

def conv(x):
    return float(x.strip().replace(",", ".").replace(" ", ""))


right_digits = list(map(conv, digits))
print(right_digits)

