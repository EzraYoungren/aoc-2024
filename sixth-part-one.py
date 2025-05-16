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

while True:
    direction = directions[direction_idx]
    x += direction[0]
    y += direction[1]
    if y >= len(lines) or y < 0 or x >= len(lines[0]) or x < 0:
        break
    char = lines[y][x]
    if char == "#":
        x -= direction[0]
        y -= direction[1]
        direction_idx = (direction_idx + 1) % 4
    else:
        lines[y][x] = "X"

ret = 0
for line in lines:
    for char in line:
        if char == "X":
            ret += 1

print(ret)
