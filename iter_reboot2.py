import runpy, time
from threading import Timer
import iter_reboot


for i in range(3):
    runpy.run_module("iter_reboot")
    print("____", iter_reboot.tt)
    time.sleep(1)
