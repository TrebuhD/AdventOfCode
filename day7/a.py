from day7.graph import Graph

input_file = open("./input.txt", "r").read().splitlines()

example_rules = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()


def get_number_of_bags(number: str) -> int:
    if number == 'no':
        return 0
    return int(number)


def parse_rules(input_rules: list[str]) -> dict:
    bag_rules = {}

    for line in input_rules:
        # the first 2 words combined are the bag type
        bag_type = ''.join(line.split(None, 2)[:2])

        if bag_type not in bag_rules:
            bag_rules[bag_type] = []

        bag_content_rules = line.split(' ')[4:]

        for idx, word in enumerate(bag_content_rules):
            try:
                can_hold_count = get_number_of_bags(word)
            except ValueError:
                # not a number
                continue

            if can_hold_count != 0:
                held_bag_type = bag_content_rules[idx + 1] + bag_content_rules[idx + 2]
                bag_rules[bag_type].append({held_bag_type: can_hold_count})

    return bag_rules


def populate_graph(bags_dict: dict) -> Graph:
    result_graph = Graph(connections=[], directed=True)
    for name, rules in bags_dict.items():
        for rule in rules:
            can_hold_bag_name, can_hold_count = rule.copy().popitem()
            result_graph.add(name, can_hold_bag_name)

    return result_graph


bags = parse_rules(input_file)
rules_graph = populate_graph(bags)

num_connected = 0
for bag_name in bags.keys():
    path = rules_graph.find_path(bag_name, 'shinygold')
    if path and len(path) > 1:
        num_connected += 1

print("result:", num_connected)
