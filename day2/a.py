lines = open("./input.txt", "r").read().splitlines()

num_passwords_valid = 0

for i, line in enumerate(lines):
    [letter_count, _letter, password] = line.split(" ")
    letter = _letter[0]
    [count_start, count_end] = [int(x) for x in letter_count.split("-")]

    num_letters_in_password = 0
    for char in password:
        if char == letter:
            num_letters_in_password += 1

    if count_start <= num_letters_in_password <= count_end:
        num_passwords_valid += 1

print("number of valid passwords: ", num_passwords_valid)
