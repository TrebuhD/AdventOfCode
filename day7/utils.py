def get_number_of_bags(number: str) -> int:
    if number == 'no':
        return 0
    return int(number)


def parse_bag_rules(input_rules: list[str]) -> dict:
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
