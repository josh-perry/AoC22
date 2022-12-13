import json


def parse_input():
    input_file = open("day_13/input", "r")
    packet_pairs = []

    packet_pair = []
    for line in input_file.readlines():
        if len(packet_pair) in (0, 1):
            packet_pair.append(json.loads(line.rstrip()))
            continue

        packet_pairs.append(packet_pair)
        packet_pair = []

    packet_pairs.append(packet_pair)
    return packet_pairs


def compare_pair(left, right):
    is_left_list = isinstance(left, list)
    is_right_list = isinstance(right, list)

    if is_left_list and not is_right_list:
        right = [right]
        is_right_list = True

    if is_right_list and not is_left_list:
        left = [left]
        is_left_list = True

    if not is_left_list and not is_right_list:
        if left == right:
            return None

        return left < right

    if is_left_list and is_right_list:
        while True:
            if len(left) == 0:
                return True

            if len(right) == 0:
                return False

            result = compare_pair(left.pop(0), right.pop(0))

            if result is not None:
                return result


def part_1():
    """
    Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
    :return:
    """
    print("Part 1")
    packet_pairs = parse_input()

    total_indices = 0

    for pair_index in range(0, len(packet_pairs)):
        pair = packet_pairs[pair_index]
        in_order = compare_pair(pair[0], pair[1])

        if in_order:
            total_indices += pair_index + 1

    print(total_indices)


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 13")
    part_1()
    part_2()
