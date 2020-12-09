input_file = open("./input.txt", "r").read().splitlines()
instruction_count = len(input_file)

visited_idx = set()
acc = 0
curr_index = 0

while True:
    if curr_index in visited_idx:
        print('instruction executed a second time.', 'acc value: ', acc)
        break
    visited_idx.add(curr_index)
    [opt, arg] = input_file[curr_index].split(' ')
    curr_index = (curr_index + 1) % instruction_count

    print("opt: ", opt, "| arg: ", arg)
    if opt == 'nop':
        continue
    if opt == 'jmp':
        curr_index += int(arg) - 1
    if opt == 'acc':
        acc += int(arg)
