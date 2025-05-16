with open("input.txt") as f:
    file = f.read()

ret = 0
lines = file.split("\n")

m_and_s = ["M", "M", "S", "S"]


def check(lines, offset, x, y):
    if x < 1 or x > len(lines[0]) - 2:
        return False
    if y < 1 or y > len(lines) - 2:
        return False

    if lines[y - 1][x - 1] == m_and_s[offset % 4]:
        if lines[y - 1][x + 1] == m_and_s[(offset + 1) % 4]:
            if lines[y + 1][x + 1] == m_and_s[(offset + 2) % 4]:
                if lines[y + 1][x - 1] == m_and_s[(offset + 3) % 4]:
                    return True


for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "A":
            for result in [
                check(lines, 1, x, y),
                check(lines, 2, x, y),
                check(lines, 3, x, y),
                check(lines, 4, x, y),
            ]:
                if result:
                    ret += 1

print(ret)
