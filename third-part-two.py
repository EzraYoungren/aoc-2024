import re

with open("input.txt") as f:
    file = f.read()

ret = 0
lines = file.split("\n")
do = True
for line in lines:
    results = re.findall(r"mul\(([0-9]*),([0-9]*)\)|(do)\(\)|(don't)\(\)", line)
    for result in results:
        n1, n2, n3, n4 = result
        if n3:
            do = True
        if n4:
            do = False
        if do and n1 and n2:
            ret += int(n1) * int(n2)

print(ret)
