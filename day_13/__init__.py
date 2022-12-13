import json
from functools import cmp_to_key


def parse_input():
    input_file = open("day_13/input", "r")
    packets = []

    for line in input_file.readlines():
        if line.isspace():
            continue

        packets.append(json.loads(line))

    return packets


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
            return 0

        return 1 if left < right else -1

    if is_left_list and is_right_list:
        for index in range(min(len(left), len(right))):
            result = compare_pair(left[index], right[index])

            if not result:
                continue

            return result

        if len(left) < len(right):
            return 1

        if len(left) > len(right):
            return -1


def part_1():
    """
    Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
    :return:
    """
    print("Part 1")
    packets = parse_input()
    packet_pairs = []

    for packet_index in range(0, len(packets), 2):
        packet_pairs.append([packets[packet_index], packets[packet_index + 1]])

    total_indices = 0

    for pair_index in range(0, len(packet_pairs)):
        pair = packet_pairs[pair_index]
        in_order = compare_pair(pair[0], pair[1]) == 1

        if in_order:
            total_indices += pair_index + 1

    print(total_indices)


def part_2():
    """
    Organize all of the packets into the correct order. What is the decoder key for the distress signal?
    :return:
    """
    print("Part 2")
    packets = parse_input()
    divider_packets = [
        [[2]],
        [[6]]
    ]

    for divider_packet in divider_packets:
        packets.append(divider_packet)

    sorted_packets = sorted(packets, key=cmp_to_key(compare_pair), reverse=True)

    decoder_key = 1
    for divider_packet in divider_packets:
        index = sorted_packets.index(divider_packet) + 1
        decoder_key *= index

    print(decoder_key)


def go():
    print("Day 13")
    part_1()
    part_2()
