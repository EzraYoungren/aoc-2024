with open("input.txt") as f:
    file = f.read()

ret = 0
lines = file.split("\n")


def check(lines, x_dir, y_dir, x, y):
    max_x = x + x_dir * 3
    max_y = y + y_dir * 3
    if max_x < 0 or max_x > len(lines[0]) - 1:
        return False
    if max_y < 0 or max_y > len(lines) - 1:
        return False

    if lines[y + y_dir][x + x_dir] == "M":
        if lines[y + y_dir * 2][x + x_dir * 2] == "A":
            if lines[y + y_dir * 3][x + x_dir * 3] == "S":
                return True


for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "X":
            for result in [
                check(lines, 1, 0, x, y),
                check(lines, 0, 1, x, y),
                check(lines, -1, 0, x, y),
                check(lines, 0, -1, x, y),
                check(lines, 1, -1, x, y),
                check(lines, -1, 1, x, y),
                check(lines, -1, -1, x, y),
                check(lines, 1, 1, x, y),
            ]:
                if result:
                    ret += 1

print(ret)
