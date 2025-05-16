with open("input.txt") as f:
    file = f.read()

lines = [[number for number in list(line)] for line in file.split("\n")]


def check(num, x, y):
    print(num, x, y)
    if x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines):
        print("ree")
        if lines[y][x] == str(num):
            if num == 9:
                print("wrath")
                return {f"{x},{y}": True}
            else:
                return {
                    # **nines,
                    **check(num + 1, x + 1, y),
                    **check(num + 1, x, y + 1),
                    **check(num + 1, x - 1, y),
                    **check(num + 1, x, y - 1),
                }
    return {}


all_nines = {}
ret = 0
for y, line in enumerate(lines):
    for x, number in enumerate(line):
        if number == "0":
            print("ra")
            res = check(0, x, y)
            for _ in res.values():
                ret += 1


print(ret)
