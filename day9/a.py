numbers = list(map(int, open("./input.txt", "r").read().splitlines()))

# skip the first 25 items
preamble_len = 25
cur_index = preamble_len

# while cur_index < 26:
while cur_index < len(numbers):
    cur_number = numbers[cur_index]
    to_sum = sorted(numbers[cur_index - preamble_len:cur_index])

    found_sum = False
    for idx, num in enumerate(to_sum):
        if num > cur_number or found_sum:
            break

        # find pair
        pair_idx = idx
        while pair_idx < len(to_sum) and to_sum[pair_idx] < cur_number and not found_sum:
            if to_sum[pair_idx] + num == cur_number and to_sum[pair_idx] != num:
                found_sum = True
                break
            pair_idx += 1

    if not found_sum:
        print("found the odd one: ", cur_number)
        break

    cur_index += 1
