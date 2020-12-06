lines = open("./input.txt", "r").read().splitlines()

num_passwords_valid = 0

for i, line in enumerate(lines):
    [indexes, _letter, password] = line.split(" ")
    letter = _letter[0]
    [indexA, indexB] = [int(x) for x in indexes.split("-")]

    match_a = password[indexA - 1] == letter
    match_b = password[indexB - 1] == letter
    # xor
    if match_a != match_b:
        num_passwords_valid += 1

print("number of valid passwords: ", num_passwords_valid)
