from datetime import datetime as dt
from datetime import timedelta
from time import sleep

class Clock:
    def __init__(self, hours=0,  minutes=0, seconds=0):
        self.time = dt(100, 1, 1, hours, minutes, seconds)

    def __next__(self):
        self.time = self.time + timedelta(seconds=1)
        with open("progress_test", "w", encoding="utf-8") as f:
            f.write(dt.now().strftime("%H:%M:%S"))
        t = dt.now().strftime("%H:%M:%S")
        sleep(1)
        return t

    def __iter__(self):
        return self


i = 1
tt = 0
for time in Clock():
    tt = time
    print(tt)
    i -= 1
    if i <= 0:
        break
