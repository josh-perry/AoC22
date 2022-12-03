import string


def parse_input():
    input_file = open("day_03/input", "r")
    all_rucksacks = []

    for line in input_file.readlines():
        rucksack = []
        total_rucksack = []

        for character in line.rstrip():
            total_rucksack.append(string.ascii_letters.find(character) + 1)

        half_index = len(total_rucksack) // 2
        rucksack.append(total_rucksack[:half_index])
        rucksack.append(total_rucksack[half_index:])

        all_rucksacks.append(rucksack)

    return all_rucksacks


def part_1():
    """
    Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those
    item types?
    :return:
    """
    print("Part 1")
    rucksacks = parse_input()
    total_priority = 0

    for rucksack in rucksacks:
        item_appearing_in_both = set(rucksack[0]).intersection(rucksack[1])
        total_priority += sum(item_appearing_in_both)

    print(total_priority)


def part_2():
    """

    :return:
    """
    print("Part 2")


def go():
    print("Day 3")
    part_1()
    part_2()
