with open("input.txt") as f:
    file = f.read()

chars = list(file)

result = []
char_id = 0

for idx, char in enumerate(chars):
    if idx % 2 == 1:
        spaces = int(char)
        for _ in range(spaces):
            result.append(".")
    else:
        size = int(char)
        for _ in range(size):
            result.append(char_id)
        char_id += 1

print(result)
actual_result = result.copy()
result.reverse()
for idx, char_id in enumerate(result):
    inverse_idx = len(actual_result) - (idx + 1)
    if char_id == ".":
        continue
    else:
        finished = False
        for aidx, achar_id in enumerate(actual_result):
            if achar_id == "." and aidx < inverse_idx:
                finished = True
                print(aidx)
                actual_result[aidx] = char_id
                break
        if not finished:
            break
        actual_result[inverse_idx] = "!"

actual_result = [number for number in actual_result if number != "!"]

print(actual_result)
ret = 0
for idx, char_id in enumerate(actual_result):
    if char_id != ".":
        ret += idx * char_id

print(ret)
