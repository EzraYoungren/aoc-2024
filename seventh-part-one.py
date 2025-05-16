with open("input.txt") as f:
    file = f.read()

lines = file.split("\n")


def calc_with_code(code, desired_number, numbers):
    if len(code) >= len(numbers):
        ret = 0
        for idx, number in enumerate(numbers):
            if code[idx] == "+":
                ret += number
            if code[idx] == "x":
                ret *= number
        if ret == desired_number:
            print(code, desired_number, numbers)
            return True
    else:
        result_one = calc_with_code(code + "+", desired_number, numbers)
        result_two = calc_with_code(code + "x", desired_number, numbers)
        return result_one or result_two


ret = 0
for line in lines:
    n1, numbers = line.split(": ")
    if calc_with_code("+", int(n1), [int(number) for number in numbers.split(" ")]):
        ret += int(n1)

print(ret)
