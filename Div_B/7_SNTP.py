import math


def time_to_int(my_str: str):
    time = 0
    arr = my_str.split(":")
    time = int(arr[0])*3600 + int(arr[1])*60 + int(arr[2])
    return time


def int_to_str(time: int):
    hh = 0
    mm = 0
    ss = 0
    while time >= 3600:
        hh += 1
        time -= 3600

    while time >= 60:
        mm += 1
        time -= 60
    ss = time
    if hh < 10:
        hh = "0" + str(hh)
    if mm < 10:
        mm = "0" + str(mm)
    if ss < 10:
        ss = "0" + str(ss)
    return f"{hh}:{mm}:{ss}"


with open('input.txt', 'r') as f:
    first_str = f.readline().strip()
    sec_str = f.readline().strip()
    third_str = f.readline().strip()


timeA = time_to_int(first_str)
timeB = time_to_int(sec_str)
timeC = time_to_int(third_str)

SECOND_IN_ONE_DAY = 86400

delay = 0

if timeA <= timeC:
    delay = (timeC - timeA)/2
else:
    delay = (timeC + SECOND_IN_ONE_DAY - timeA)/2

delay = math.ceil(delay)

if timeB+delay >= SECOND_IN_ONE_DAY:
    timeB = timeB + delay - SECOND_IN_ONE_DAY
else:
    timeB = timeB + delay

out = open('output.txt', 'w')
out.write(int_to_str(timeB))
out.close()
