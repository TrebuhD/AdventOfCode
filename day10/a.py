numbers = list(map(int, open("./input.txt", "r").read().splitlines()))

max_n = max(numbers)
device_max_joltage = max_n + 3

# store the number of jolt differences inside chain
differences = {'one': 0, 'three': 0}
outlet_joltage = 0


def get_differences(joltages, joltage_differences, input_joltage):
    if input_joltage + 1 in joltages:
        joltage_differences['one'] += 1
        get_differences(joltages, joltage_differences, input_joltage + 1)
    elif input_joltage + 2 in joltages:
        get_differences(joltages, joltage_differences, input_joltage + 2)
    elif input_joltage + 3 in joltages:
        joltage_differences['three'] += 1
        get_differences(joltages, joltage_differences, input_joltage + 3)
    if input_joltage + 3 == device_max_joltage:
        joltage_differences['three'] += 1


get_differences(numbers, differences, outlet_joltage)
print("differences: ", differences)
print("a): ", differences['one'] * differences['three'])
