input_lines = open("./input.txt", "r").read().splitlines()

visited_idx = set()
acc = 0
curr_index = 0
reached_end = False

# indices of lines that contain 'jmp' and 'nop' instructions
nop_jmp_indices = [i for i, x in enumerate(input_lines) if x.split(' ')[0] in ('nop', 'jmp')]
curr_flipped_idx = 0


def get_flipped_instruction(instruction):
    [o, a] = instruction.split(' ')
    new_opt = 'jmp' if o == 'nop' else 'nop'
    return ''.join([new_opt, ' ', a])


def flip_instruction(i):
    """ Mutates the input_lines array.
    Changes instructions from nop -> jmp and reverse.
    """
    to_flip_index = nop_jmp_indices[i]
    new_instruction = get_flipped_instruction(input_lines[to_flip_index])
    input_lines[to_flip_index] = new_instruction


while True:
    if reached_end:
        print('program terminated. acc: ', acc)
        break

    # loop detected. Try again, flipping another instruction
    if curr_index in visited_idx:
        flip_instruction(curr_flipped_idx)
        if curr_flipped_idx != 0:
            # flip back previous instruction
            flip_instruction(curr_flipped_idx - 1)
        curr_flipped_idx += 1
        # restart program
        visited_idx = set()
        curr_index = 0
        acc = 0
        continue
    visited_idx.add(curr_index)

    if curr_index == len(input_lines) - 1:
        reached_end = True

    [opt, arg] = input_lines[curr_index].split(' ')
    curr_index = (curr_index + 1) % len(input_lines)

    if opt == 'nop':
        continue
    if opt == 'jmp':
        curr_index += int(arg) - 1
    if opt == 'acc':
        acc += int(arg)
