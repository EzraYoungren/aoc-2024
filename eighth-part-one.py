with open("input.txt") as f:
    file = f.read()

lines = [list(line) for line in file.split("\n")]
frequencies = {}

max_x = len(lines[0])
max_y = len(lines)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            if char not in frequencies:
                frequencies[char] = [(x, y)]
            else:
                frequencies[char].append((x, y))

ret = 0
print(frequencies)
for frequency in frequencies.values():
    lines_copy = [line.copy() for line in lines.copy()]
    for v1 in frequency:
        for v2 in frequency:
            if v1 == v2:
                continue
            (v1x, v1y) = v1
            (v2x, v2y) = v2
            x_dir = v1x - v2x
            y_dir = v1y - v2y
            an1x = v1x + x_dir
            an1y = v1y + y_dir
            an2x = v2x - x_dir
            an2y = v2y - y_dir
            if an1x < max_x and an1x >= 0 and an1y < max_y and an1y >= 0:
                if lines_copy[an1y][an1x] == ".":
                    lines_copy[an1y][an1x] = "#"
            if an2x < max_x and an2x >= 0 and an2y < max_y and an2y >= 0:
                if lines_copy[an2y][an2x] == ".":
                    lines_copy[an2y][an2x] = "#"

    for line in lines_copy:
        for char in line:
            if char == "#":
                ret += 1

print(lines)

print(ret)
ret = [
    [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    [".", ".", ".", "#", ".", ".", ".", ".", "0", ".", ".", "."],
    [".", ".", ".", ".", "#", "0", ".", ".", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", ".", ".", "0", ".", ".", ".", "."],
    [".", ".", ".", ".", "0", ".", ".", ".", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", ".", "A", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
]
