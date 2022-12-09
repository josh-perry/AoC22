import re
from dataclasses import dataclass


@dataclass
class Instruction:
    direction: str
    distance: int


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


def parse_input():
    input_file = open("day_09/input", "r")
    instruction_regex = r"(U|D|L|R) (\d+)"

    instructions = []

    for line in input_file.readlines():
        match = re.match(instruction_regex, line)
        groups = match.groups()

        direction = groups[0]
        distance = int(groups[1])

        instructions.append(Instruction(direction, distance))

    return instructions


def is_touching(p1, p2):
    return abs(p1.x - p2.x) <= 1 and abs(p1.y - p2.y) <= 1


def part_1():
    """
    Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least
    once?
    :return:
    """
    print("Part 1")
    instructions = parse_input()
    head_position = Position(0, 0)
    last_head_position = Position(0, 0)
    tail_position = Position(0, 0)

    direction_offsets = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    tail_visits = set()
    tail_visits.add((tail_position.x, tail_position.y))

    for instruction in instructions:
        offset = direction_offsets[instruction.direction]

        for step in range(0, instruction.distance):
            last_head_position.x = head_position.x
            last_head_position.y = head_position.y
            head_position += offset

            if is_touching(head_position, tail_position):
                continue

            tail_position.x = last_head_position.x
            tail_position.y = last_head_position.y
            tail_visits.add((tail_position.x, tail_position.y))

    print(len(tail_visits))


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 9")
    part_1()
    part_2()
