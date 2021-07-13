import time
from datetime import datetime
from datetime import timedelta
from time import strptime, strftime

current_time = datetime.now()

time_file = open("times.txt", 'w+')


def log_time():
    time_file.write(str(current_time.strftime('%H')))
    time_file.seek(0)


def previous_time():
    prev_time = time_file.read()
    return strptime(prev_time, "%H")

log_time()
