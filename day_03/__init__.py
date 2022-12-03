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


def find_common_item(rucksacks):
    common_items = list(set.intersection(*[set(x) for x in rucksacks]))
    return common_items[0]


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
        common_item = find_common_item([rucksack[0], rucksack[1]])
        total_priority += common_item

    print(total_priority)


def part_2():
    """
    Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of
    those item types?
    :return:
    """
    print("Part 2")
    rucksacks = parse_input()
    total_priority = 0

    for rucksack_index in range(0, len(rucksacks), 3):
        group_rucksacks = [
            rucksacks[rucksack_index + 0][0] + rucksacks[rucksack_index + 0][1],
            rucksacks[rucksack_index + 1][0] + rucksacks[rucksack_index + 1][1],
            rucksacks[rucksack_index + 2][0] + rucksacks[rucksack_index + 2][1],
        ]

        total_priority += find_common_item(group_rucksacks)

    print(total_priority)


def go():
    print("Day 3")
    part_1()
    part_2()
