def read_file(path):
    binary_numbers = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            binary_numbers.append(line.strip())
    return binary_numbers


def task_two(path):
    binary_numbers = read_file(path)
    numbers_divisible_by_two = 0
    numbers_divisible_by_eight = 0
    for number in binary_numbers:
        if number[-1] == '0':
            numbers_divisible_by_two += 1
        if (len(number) == 1 and number[-1] == '0') or (len(number) >= 3 and number[-3:] == '000'):
            numbers_divisible_by_eight += 1

    return numbers_divisible_by_two, numbers_divisible_by_eight
