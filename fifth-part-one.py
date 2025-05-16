with open("input.txt") as f:
    file = f.read()

rules_obj = {}
ret = 0
rules, updates = file.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")
for rule in rules:
    n1, n2 = rule.split("|")
    if n1 not in rules_obj:
        rules_obj[n1] = [n2]
    else:
        rules_obj[n1].append(n2)

print(rules_obj)
for update in updates:
    numbers = update.split(",")
    bad_update = False
    for idx, number in enumerate(numbers):
        if number not in rules_obj:
            continue
        needed = rules_obj[number].copy()
        for other_number in numbers[:idx]:
            if other_number in needed:
                bad_update = True
                break

    if not bad_update:
        ret += int(numbers[int(len(numbers) / 2)])

print(ret)
