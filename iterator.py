class Fib:
    def __init__(self, max_items=4):
        self.max_items = max_items

    def __next__(self):
        self.items += 1
        if self.max_items == self.items:
            raise StopIteration

        self.fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return self.fib

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.items = -1
        return self


for item in Fib(5):
    print(item)
