from day7.graph import Graph
from day7.utils import parse_bag_rules

input_file = open("./input.txt", "r").read().splitlines()


def populate_graph(bags_dict: dict) -> Graph:
    result_graph = Graph(connections=[], directed=True)
    for name, rules in bags_dict.items():
        for rule in rules:
            can_hold_bag_name, can_hold_count = rule.copy().popitem()
            result_graph.add(name, can_hold_bag_name)

    return result_graph


bags = parse_bag_rules(input_file)
print(bags)

rules_graph = populate_graph(bags)

num_connected = 0
for bag_name in bags.keys():
    path = rules_graph.find_path(bag_name, 'shinygold')
    if path and len(path) > 1:
        num_connected += 1

print("a) result:", num_connected)
