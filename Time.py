from pathlib import Path
from datetime import datetime
import os
import time


def clock(hour, minute, second):
    os.system('clear')
    print(hour, ':', minute, ':', second)
    if (int(second) + 1 == 60):
        minute = (int(minute) + 1) % 60
        if (int(minute) == 0):
            hour = (int(hour) + 1) % 12
            if (int(hour == 0)):
                hour = 12
    second = (int(second) + 1) % 60
    time.sleep(1)
    os.system('clear')
    clock(hour, minute, second)


now = datetime.now()
hour = now.strftime("%H")
hour = int(hour) % 12
minute = now.strftime("%M")
second = now.strftime("%S")
clock(hour, minute, second)
