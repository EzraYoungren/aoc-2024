import re

with open("input.txt") as f:
    file = f.read()

arr = [int(number) for number in file.split(" ")]
new_arr = []
for _ in range(25):
    for number in arr:
        print(number)
        str_length = len(str(number))
        if number == 0:
            new_arr.append(1)
        elif str_length % 2 == 0:
            new_arr.append(int(str(number)[: int(str_length / 2)]))
            new_arr.append(int(str(number)[int(str_length / 2) :]))
        else:
            new_arr.append(number * 2024)
    arr = new_arr
    new_arr = []

print(len(arr))
