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

bad_updates = []
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

    if bad_update:
        bad_updates.append(numbers)

print(bad_updates)
for bad_update in bad_updates:
    sorted_update = []
    for number in bad_update:
        if number not in rules_obj:
            sorted_update.append(number)
            continue
        before = rules_obj[number]
        ended = False
        for idx, sorted_number in enumerate(sorted_update):
            if sorted_number in before:
                ended = True
                sorted_update.insert(idx, number)
                break
        if not ended:
            sorted_update.append(number)
    print(sorted_update)
    ret += int(sorted_update[int(len(sorted_update) / 2)])


print(ret)
