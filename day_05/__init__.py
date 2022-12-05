import re
from dataclasses import dataclass


@dataclass
class Instruction:
    amount_to_move: int
    source_stack_index: int
    destination_stack_index: int


def resize_stacks_to_capacity(stacks, maximum):
    for i in range(len(stacks), maximum):
        stacks.append([])


def parse_initial_stacks():
    input_file = open("day_05/input", "r")
    stacks = []
    stack_regex = r"\[(.?)\]"

    for line in input_file.readlines():
        for match in re.finditer(stack_regex, line):
            stack_index = match.start() // 4
            resize_stacks_to_capacity(stacks, stack_index + 1)

            box_substring = match.string[match.start():match.end()]
            box_label = re.match(stack_regex, box_substring).groups()[0]
            stacks[stack_index].append(box_label)

        if line.isspace():
            break

    for stack in stacks:
        stack.reverse()

    return stacks


def parse_instructions():
    input_file = open("day_05/input", "r")
    instructions = []
    instruction_regex = r"move (\d+) from (\d+) to (\d+)"

    for line in input_file.readlines():
        matches = re.match(instruction_regex, line)

        if not matches:
            continue

        match_groups = matches.groups()

        amount_to_move = int(match_groups[0])
        source_stack_index = int(match_groups[1]) - 1
        destination_stack_index = int(match_groups[2]) - 1

        instruction = Instruction(amount_to_move, source_stack_index, destination_stack_index)
        instructions.append(instruction)

    return instructions


def execute_instructions_one_by_one(stacks, instructions):
    for instruction in instructions:
        for i in range(0, instruction.amount_to_move):
            box = stacks[instruction.source_stack_index].pop()
            stacks[instruction.destination_stack_index].append(box)


def execute_instructions_batched(stacks, instructions):
    for instruction in instructions:
        source_stack = stacks[instruction.source_stack_index]
        batch_to_move = source_stack[len(source_stack) - instruction.amount_to_move:len(source_stack)]

        stacks[instruction.destination_stack_index] += batch_to_move
        stacks[instruction.source_stack_index] = source_stack[:len(source_stack) - len(batch_to_move)]


def part_1():
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    :return:
    """
    print("Part 1")
    stacks = parse_initial_stacks()
    instructions = parse_instructions()
    execute_instructions_one_by_one(stacks, instructions)

    print("".join(map(lambda s: s[len(s) - 1], stacks)))


def part_2():
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    :return:
    """
    print("Part 2")
    stacks = parse_initial_stacks()
    instructions = parse_instructions()
    execute_instructions_batched(stacks, instructions)

    print("".join(map(lambda s: s[len(s) - 1], stacks)))


def go():
    print("Day 5")
    part_1()
    part_2()
