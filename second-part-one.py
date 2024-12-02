with open("input.txt") as f:
    file = f.read()

lines = file.split("\n")

ret = 0
for line in lines:
    prev = -1
    is_inc = False
    is_dec = False
    is_safe = True
    for num in line.split(" "):
        if prev == -1:
            prev = int(num)
            continue

        if prev > int(num):
            if is_inc:
                is_safe = False
                break
            is_dec = True
        if prev < int(num):
            if is_dec:
                is_safe = False
                break
            is_inc = True

        if abs(int(num) - prev) > 3 or abs(int(num) - prev) == 0:
            is_safe = False
            break

        prev = int(num)

    if is_safe:
        print(line)
        ret += 1

print(ret)
