from datetime import datetime, timedelta
import time

class Clock:
    def __init__(self, h=0, m=0, s=0):
        self.h, self.m, self.s = h, m, s

    def __next__(self):
        with open("progress", "a", encoding="utf-8"):
            while True:
                task_name = input("Task_name: ")
                if len(task_name) < 3:
                    print("The task name is too short")
                else:
                    start_time = time.time()

                    while True:
                        task_completed = input(f'Time is running. Press y if the "{task_name.upper()}" is completed: ')
                        if task_completed == "y":
                            return time.time() - start_time



    def __iter__(self):
        return self


clock = Clock()
print(clock.__next__())
print(clock.__next__())
print(clock.__next__())
