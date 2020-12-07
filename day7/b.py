from day7.utils import parse_bag_rules

input_file = open("./input.txt", "r").read().splitlines()

bags = parse_bag_rules(input_file)


def get_bag_count(bag_name: str) -> int:
    result = 1
    for bag in bags[bag_name]:
        bag_name, bag_count = bag.copy().popitem()
        result += get_bag_count(bag_name) * bag_count

    return result


# subtract the single shinygold bag
answer = get_bag_count('shinygold') - 1
print(answer)
