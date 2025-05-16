import re

with open("input.txt") as f:
    file = f.read()

log = {}


def evaluate(number, log, range_amount):
    log[number] = {}
    cached = 0
    arr = [number]
    new_arr = []
    for idx in range(range_amount):
        print(idx)
        for n2 in arr:
            str_length = len(str(n2))
            if n2 in log:
                if 75 - idx in log[n2]:
                    cached += log[n2][75 - idx]
            if n2 == 0:
                new_arr.append(1)
            elif str_length % 2 == 0:
                new_arr.append(int(str(n2)[: int(str_length / 2)]))
                new_arr.append(int(str(n2)[int(str_length / 2) :]))
            else:
                new_arr.append(n2 * 2024)
        arr = new_arr
        log[number][idx] = len(arr) + cached
        new_arr = []

    return log


for number in range(75):
    for idx in range(12):
        log = evaluate(idx, log, number)

cached = 0
arr = [int(number) for number in file.split(" ")]
new_arr = []
for idx in range(75):
    # print(idx)
    for number in arr:
        str_length = len(str(number))
        if number in log:
            if 75 - idx in log[number]:
                cached += log[number][75 - idx]

        if number == 0:
            new_arr.append(1)
        elif str_length % 2 == 0:
            new_arr.append(int(str(number)[: int(str_length / 2)]))
            new_arr.append(int(str(number)[int(str_length / 2) :]))
        else:
            new_arr.append(number * 2024)
    arr = new_arr
    new_arr = []

print(log, len(arr), cached, len(arr) + cached)
