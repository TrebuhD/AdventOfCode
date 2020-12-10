numbers = list(map(int, open("./input.txt", "r").read().splitlines()))


def find_odd_one():
    # skip the first 25 items
    preamble_len = 25
    cur_index = preamble_len
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
            return cur_number

        cur_index += 1


odd_one = find_odd_one()
print('a) First invalid number:', odd_one)


def find_range(sum_to):
    """ returns a list of numbers that sum up to odd_one """
    # start with a range of two items
    range_len = 2
    range_idx_a = 0

    while True:
        range_idx_b = range_idx_a + range_len
        if range_len == len(numbers):
            print("sum not found. Exiting")
            break
        if range_idx_b == len(numbers):
            # reached the end for this range length
            range_len += 1
            range_idx_a = 0
            continue
        num_range = numbers[range_idx_a:range_idx_b]
        sum_range = sum(num_range)
        if sum_range == sum_to:
            print("\nthe range:", num_range)
            return num_range
        else:
            range_idx_a += 1


r = find_range(odd_one)

print('b) Sum:', min(r) + max(r))
