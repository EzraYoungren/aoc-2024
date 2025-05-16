import re

with open("input.txt") as f:
    file = f.read()

ret = 0
lines = file.split("\n")
for line in lines:
    results = re.findall(r"mul\(([0-9]*),([0-9]*)\)", line)
    for result in results:
        n1, n2 = result
        ret += int(n1) * int(n2)

print(ret)
