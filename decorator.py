def register_call(func):
    def wrapper(*args, **kwargs):
        print("->> call {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@register_call
def square(x):
    return x ** 2


@register_call
def cube(x):
    return x ** 3


print(square(5))
print(cube(5))
