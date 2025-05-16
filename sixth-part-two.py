import json

with open("input.txt") as f:
    file = f.read()

lines = [list(line) for line in file.split("\n")]
x = 0
y = 0
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
direction_idx = 0
for line_y, line in enumerate(lines):
    for char_x, char in enumerate(line):
        if char == "^":
            x = char_x
            y = line_y

log = {f"{x},{y}": [direction_idx]}


def find_similar(lines_copy, x, y, direction_idx, log_copy):
    while True:
        x_dir, y_dir = directions[direction_idx]
        x += x_dir
        y += y_dir

        if y >= len(lines_copy) or y < 0 or x >= len(lines_copy[0]) or x < 0:
            return False

        char = lines_copy[y][x]

        if char == "#":
            x -= x_dir
            y -= y_dir
            direction_idx = (direction_idx + 1) % 4
            continue
        elif f"{x},{y}" in log_copy:
            if direction_idx in log_copy[f"{x},{y}"]:
                return True

        if f"{x},{y}" not in log_copy:
            log_copy[f"{x},{y}"] = [direction_idx]
        else:
            log_copy[f"{x},{y}"].append(direction_idx)


while True:
    x_dir, y_dir = directions[direction_idx]
    if f"{x},{y}" not in log:
        log[f"{x},{y}"] = [direction_idx]
    elif direction_idx not in [f"{x},{y}"]:
        log[f"{x},{y}"].append(direction_idx)

    if not (
        y + y_dir >= len(lines)
        or y + y_dir < 0
        or x + x_dir >= len(lines[0])
        or x + x_dir < 0
    ):
        copy = {}
        for key, entry in log.items():
            copy[key] = entry.copy()
        lines_copy = [line.copy() for line in lines.copy()]
        lines_copy[y + y_dir][x + x_dir] = "#"
        if (
            find_similar(lines_copy, x, y, (direction_idx + 1) % 4, copy)
            and lines[y + y_dir][x + x_dir] != "^"
            and lines[y + y_dir][x + x_dir] != "#"
            and not f"{x + x_dir},{y + y_dir}" in log
        ):
            lines[y + y_dir][x + x_dir] = "O"

    x += x_dir
    y += y_dir
    print(x, y)
    if y >= len(lines) or y < 0 or x >= len(lines[0]) or x < 0:
        break
    char = lines[y][x]
    if char == "#":
        x -= x_dir
        y -= y_dir
        direction_idx = (direction_idx + 1) % 4
        continue
    # else:

ret = 0
for line in lines:
    for char in line:
        if char == "O":
            ret += 1

print("\n".join(["".join(line) for line in lines]))
print(ret)

f = [
    [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", "O", "^", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "O", "O", "#", "."],
    ["#", "O", ".", "O", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", "O", ".", "."],
]
