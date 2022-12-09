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


def count_tail_visits_for_rope_length(instructions, rope_length):
    rope_positions = []

    for rope_position_index in range(0, rope_length):
        rope_positions.append(Position(0, 0))

    direction_offsets = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    tail = rope_positions[-1]
    head = rope_positions[0]

    tail_visits = set()
    tail_visits.add((tail.x, tail.y))

    for instruction in instructions:
        offset = direction_offsets[instruction.direction]

        for d in range(0, instruction.distance):
            head += offset

            for i in range(1, rope_length):
                head_knot = rope_positions[i - 1]
                knot = rope_positions[i]

                if is_touching(knot, head_knot):
                    continue

                if head_knot.x - knot.x > 0:
                    knot.x += 1
                elif head_knot.x - knot.x < 0:
                    knot.x -= 1

                if head_knot.y - knot.y > 0:
                    knot.y += 1
                elif head_knot.y - knot.y < 0:
                    knot.y -= 1

                tail_visits.add((tail.x, tail.y))

    return len(tail_visits)


def part_1():
    """
    Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least
    once?
    :return:
    """
    print("Part 1")
    instructions = parse_input()

    print(count_tail_visits_for_rope_length(instructions, 2))


def part_2():
    """
    Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the
    rope visit at least once?
    :return:
    """
    print("Part 2")
    instructions = parse_input()

    print(count_tail_visits_for_rope_length(instructions, 10))


def go():
    print("Day 9")
    part_1()
    part_2()
