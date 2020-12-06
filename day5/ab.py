input_file = open("./input.txt", "r").read().splitlines()

NUM_ROWS = 128
NUM_COLS = 8

dirs = {
    'left': "L",
    'right': "R",
    'down': "F",
    'up': "B",
}


def get_row_number(string):
    rows = list(range(0, NUM_ROWS))

    for s in string:
        half_point = int(len(rows) / 2)
        if s == dirs['down']:
            rows = rows[:half_point]
        elif s == dirs['up']:
            rows = rows[half_point:]

    return rows[0]


def get_col_number(string):
    cols = list(range(0, NUM_COLS))

    for s in string:
        half_point = int(len(cols) / 2)
        if s == dirs['left']:
            cols = cols[:half_point]
        elif s == dirs['right']:
            cols = cols[half_point:]

    return cols[0]


def get_seat_id(boarding_pass):
    rows = boarding_pass[:-3]
    cols = boarding_pass[-3:]
    row = get_row_number(rows)
    col = get_col_number(cols)
    return row * 8 + col


seat_ids = list(map(get_seat_id, input_file))

print("A) Max seat id: ", max(seat_ids))


def find_my_seat():
    seat_ids.sort()
    for idx, seat_id in enumerate(seat_ids):
        next_seat_id = seat_ids[idx + 1]
        if next_seat_id != seat_id + 1:
            # found missing seat
            return int((seat_id + next_seat_id) / 2)


print("B) My seat id: ", find_my_seat())
