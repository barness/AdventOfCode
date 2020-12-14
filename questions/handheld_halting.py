def accumulator_value(instructions):
    index = 0
    accumulator = 0
    checked_index = set()
    infinite_loop = False
    prev_index = 0
    while True:
        if index in checked_index:
            infinite_loop = True
            return [infinite_loop, accumulator, prev_index]
        if index > len(instructions) - 1:
            return [infinite_loop, accumulator, prev_index]
        prev_index = index
        action_value = instructions[index].split()
        checked_index.add(index)
        if action_value[0] == "jmp":
            index += parse_value(action_value[1])
        elif action_value[0] == "acc":
            accumulator += parse_value(action_value[1])
            index += 1
        else:
            index += 1


def accumulator_value_2():
    instructions = parse_input_file()
    index = 0

    for instruction in instructions:
        if instruction[:3] == "jmp":
            instructions[index] = "nop" + instructions[index][3:]
            with_proposed_change = accumulator_value(instructions)
            instructions[index] = "jmp" + instructions[index][3:]
            if not with_proposed_change[0]:
                return with_proposed_change
        elif instruction[:3] == "nop":
            instructions[index] = "jmp" + instructions[index][3:]
            with_proposed_change = accumulator_value(instructions)
            instructions[index] = "nop" + instructions[index][3:]
            if not with_proposed_change[0]:
                return with_proposed_change
        index += 1
    return "impossible to fix with one change to nop or jmp"


def get_prev_nop(index, instructions, tried_nops_to_jmp):
    while index >= 0:
        action_value = instructions[index].split()
        if action_value[0] == "nop" and action_value[1] in tried_nops_to_jmp:
            return action_value[1]
        index -= 1
    return "No possible answer"


def parse_value(input):
    if input[0] == "+":
        return int(input[0:])
    return int(input)


def parse_input_file():
    with open("/app/inputs/handheld_halting.txt", "r") as input_file:
        instructions = []
        for line in input_file:
            instructions.append(line)
        return instructions


if __name__ == "__main__":
    print("The value of the accumulator before it infinately loops is ", accumulator_value(parse_input_file())[1])
    print("The value of the accumulator when it finishes after fixing nop, or jmp ", accumulator_value_2()[1])
