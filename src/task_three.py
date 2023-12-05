def read_file(path):
    binary_numbers = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            binary_numbers.append(line.strip())
    return binary_numbers


def is_bigger(a, b):
    a_digits_count = len(a)
    b_digits_count = len(b)
    if a_digits_count > b_digits_count:
        return True
    elif b_digits_count > a_digits_count:
        return False
    else:
        for i in range(0, a_digits_count):
            if a[i] > b[i]:
                return True
            elif b[i] > a[i]:
                return False
    return False


def task_three(path):
    binary_numbers = read_file(path)
    biggest_index = 0
    biggest = binary_numbers[0]
    smallest_index = 0
    smallest = binary_numbers[0]
    for i in range(1, len(binary_numbers)):
        if is_bigger(binary_numbers[i], biggest):
            biggest = binary_numbers[i]
            biggest_index = i
        elif not is_bigger(binary_numbers[i], smallest):
            smallest = binary_numbers[i]
            smallest_index = i

    return smallest_index + 1, biggest_index + 1
