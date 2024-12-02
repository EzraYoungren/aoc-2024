with open("input.txt") as f:
    file = f.read()

lines = file.split("\n")

ret = 0
for line in lines:
    good_level = False
    for idx in range(-1, len(line.split(" "))):
        copy = line.split(" ").copy()
        if idx != -1:
            copy.pop(idx)
        print(line, copy)
        prev = -1
        is_inc = False
        is_dec = False
        is_safe = True
        bad_levels = 0
        for num in copy:
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
            good_level = True
            print("safe!")
            break

    if good_level:
        ret += 1

print(ret)
