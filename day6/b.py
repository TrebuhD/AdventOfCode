import functools

input_file = open("./input.txt", "r").read().splitlines()


def count_same_answers(answers):
    repeating_items = functools.reduce(lambda a, b: set(a).intersection(b), answers)
    return len(repeating_items)


def get_count_sum():
    counts = 0
    lines = []
    for line in input_file:
        if line == '':
            counts += count_same_answers(lines)
            lines = []
        else:
            lines.append(''.join(sorted(line)))
    counts += count_same_answers(lines)
    return counts


print("B) Sum of answer counts: ", get_count_sum())
