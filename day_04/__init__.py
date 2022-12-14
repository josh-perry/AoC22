import re
from dataclasses import dataclass


@dataclass
class Elf:
    first_section: int
    last_section: int


def parse_input():
    input_file = open("day_04/input", "r")
    elf_pairs = []

    for line in input_file.readlines():
        section_ids = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()
        elf_pairs.append([
            Elf(int(section_ids[0]), int(section_ids[1])),
            Elf(int(section_ids[2]), int(section_ids[3]))
        ])

    return elf_pairs


def check_contains(pair):
    first = pair[0]
    second = pair[1]

    return first.first_section >= second.first_section and first.last_section <= second.last_section or \
           first.first_section <= second.first_section and first.last_section >= second.last_section


def check_overlaps(pair):
    first = pair[0]
    second = pair[1]

    return second.first_section <= first.first_section <= second.last_section or \
           second.first_section <= first.last_section <= second.last_section


def part_1():
    """
    In how many assignment pairs does one range fully contain the other?
    :return:
    """
    print("Part 1")
    elf_pairs = parse_input()
    conflicts = 0

    for pair in elf_pairs:
        if check_contains(pair):
            conflicts += 1

    print(conflicts)


def part_2():
    """
    In how many assignment pairs do the ranges overlap?
    :return:
    """
    print("Part 2")
    elf_pairs = parse_input()
    conflicts = 0

    for pair in elf_pairs:
        if check_contains(pair) or check_overlaps(pair):
            conflicts += 1

    print(conflicts)


def go():
    print("Day 4")
    part_1()
    part_2()
