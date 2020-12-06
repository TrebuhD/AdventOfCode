input_file = open("./input.txt", "r").read().splitlines()


def get_count_sum():
    counts = 0
    current_group = set()
    for line in input_file:
        if line == '':
            counts += len(current_group)
            # reset set
            current_group = set()
        for char in line:
            current_group.add(char)
    counts += len(current_group)
    return counts


print("A) Sum of answer counts: ", get_count_sum())
