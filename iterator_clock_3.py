from datetime import datetime as dt
from datetime import timedelta
from time import sleep

class Clock:
    def __init__(self, hours=0,  minutes=0, seconds=0):
        self.time = dt(100, 1, 1, hours, minutes, seconds)

    def __next__(self):
        result = self.time
        self.time = self.time + timedelta(seconds=1)
        # Максимум для года - это 9999.
        if self.time.year > 100:
            self.time = dt(100, 1, 1, self.time.hour, self.time.minute, self.time.second)
        sleep(1)
        return result.strftime("%H:%M:%S")

    def __iter__(self):
        return self

if __name__ == "__main__":
    i = 9999999999999999999999
    for time in Clock():
        print(time)
        i -= 1
        if i <= 0:
            break
