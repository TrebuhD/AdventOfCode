import time

input_file = open("./input.txt", "r").read().splitlines()

instructions = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines()

instruction_count = len(instructions)

executed_indexes = set()
# accumulator
acc = 0
curr_index = 0

while True:
    time.sleep(0.05)
    if curr_index in executed_indexes:
        print('instruction executed a second time.', curr_index)
        print('acc value: ', acc)
        break
    executed_indexes.add(curr_index)
    instruction = instructions[curr_index]
    curr_index = (curr_index + 1) % instruction_count
    [opt, arg] = instruction.split(' ')
    if opt == 'nop':
        continue
    print("opt: ", opt, "| arg: ", arg)
    if opt == 'jmp':
        curr_index += int(arg) - 1
    if opt == 'acc':
        acc += int(arg)
