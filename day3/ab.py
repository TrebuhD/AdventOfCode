lines = open("./input.txt", "r").read().splitlines()

pattern_length = len(lines[0])


def get_tree_count(x_offset, y_offset):
    current_pos_x = 0
    current_pos_y = 0
    current_item = lines[current_pos_y][current_pos_x]
    num_trees = 0

    while current_item:
        current_pos_x += x_offset
        current_pos_y += y_offset
        try:
            current_item = lines[current_pos_y][current_pos_x % pattern_length]
        except IndexError:
            current_item = None
        if current_item == '#':
            num_trees += 1
    return num_trees


print("3, 1: ", get_tree_count(3, 1))
print("2, 2: ", get_tree_count(2, 2))
print("1, 1: ", get_tree_count(1, 1))
