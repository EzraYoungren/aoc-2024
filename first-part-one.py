with open("input.txt") as f:
    file = f.read()

lines = file.split("\n")

group_a = []
group_b = []
for line in lines:
    a, b = line.split("   ")
    group_a.append(int(a))
    group_b.append(int(b))

group_a.sort()
group_b.sort()

ret = 0
for idx, num in enumerate(group_a):
    ret += abs(num - group_b[idx])

print(ret)
