from time import sleep

class Clock:
    def __init__(self, h=0, m=0, s=0):
        self.h, self.m, self.s = h, m, s

    def __next__(self):
        t = f"{self.h:02.0f}:{self.m:02.0f}:{self.s:02.0f}"
        if self.s == 59:
            self.s = -1
            self.m += 1
        if self.m == 60:
            self.m = 0
            self.h += 1
        if self.h > 23:
            self.h = 0
        self.s += 1
        sleep(1)
        return t

    def __iter__(self):
        return self

for time in Clock():
    print(time)

if __name__ == "__main__":
    i = 4
    for time in Clock():
        print(time)
        i -= 1
        if i <= 0:
            break
