with open("input.txt") as f:
    file = f.read()

lines = file.split("\n")


def get_num(num, arr):
    ret = 0
    for part in arr:
        if num == part:
            ret += 1
    return ret


group_a = []
group_b = []
for line in lines:
    a, b = line.split("   ")
    group_a.append(int(a))
    group_b.append(int(b))

ret = 0
for idx, num in enumerate(group_a):
    count_b = get_num(num, group_b)
    ret += count_b * num

print(ret)
