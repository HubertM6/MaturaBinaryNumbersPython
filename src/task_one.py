def read_file(path):
    binary_numbers = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            binary_numbers.append(line.strip())
    return binary_numbers


def more_zeros(line):
    zeros = 0
    ones = 0
    for char in line:
        if char == '0':
            zeros += 1
        else:
            ones += 1
    return zeros > ones


def task_one(path):
    binary_numbers = read_file(path)
    numbers_having_more_zeros = 0
    for number in binary_numbers:
        if more_zeros(number):
            numbers_having_more_zeros += 1

    return numbers_having_more_zeros
