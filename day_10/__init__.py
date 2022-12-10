from dataclasses import dataclass


@dataclass
class Instruction:
    mnemonic: str
    value: int
    cycles: int


class Cpu:
    def __init__(self):
        self.x = 1
        self.cycles = 0

    def execute_instruction(self, instruction):
        if instruction.mnemonic == "addx":
            self.x += instruction.value


def parse_input():
    input_file = open("day_10/input", "r")
    instructions = []
    cycles = {
        "addx": 2,
        "noop": 1
    }

    for line in input_file.readlines():
        split_line = line.rstrip().split(" ")

        mnemonic = split_line[0]
        value = int(split_line[1]) if len(split_line) > 1 else None

        instructions.append(Instruction(mnemonic, value, cycles[mnemonic]))

    return instructions


def part_1():
    """
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six
    signal strengths?
    :return:
    """
    print("Part 1")
    cpu = Cpu()
    instructions = parse_input()
    cycle_interval_start = 20
    cycle_interval = 40
    total_signal_strength = 0

    for instruction in instructions:
        for cycle in range(0, instruction.cycles):
            cpu.cycles += 1

            if (cpu.cycles - cycle_interval_start) % cycle_interval == 0:
                signal_strength = cpu.cycles * cpu.x
                total_signal_strength += signal_strength

        cpu.execute_instruction(instruction)

    print(total_signal_strength)


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 10")
    part_1()
    part_2()
