def parse_input():
    input_file = open("day_06/input", "r")
    return input_file.read()


def find_distinct_characters_in_groups(signal, group_length):
    for index in range(group_length, len(signal)):
        signal_segment = signal[index-group_length:index+1]
        signal_segment_set = set(signal_segment)

        if len(signal_segment_set) == group_length + 1:
            return index


def part_1():
    """
    How many characters need to be processed before the first start-of-packet marker is detected?
    :return:
    """
    print("Part 1")
    signal = parse_input()
    marker_index = find_distinct_characters_in_groups(signal, 4)

    print(marker_index)


def part_2():
    """
    How many characters need to be processed before the first start-of-message marker is detected?
    :return:
    """
    print("Part 1")
    signal = parse_input()
    marker_index = find_distinct_characters_in_groups(signal, 14)

    print(marker_index)


def go():
    print("Day 6")
    part_1()
    part_2()
