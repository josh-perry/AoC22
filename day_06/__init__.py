def parse_input():
    input_file = open("day_06/input", "r")
    return input_file.read()


def part_1():
    """
    How many characters need to be processed before the first start-of-packet marker is detected?
    :return:
    """
    print("Part 1")
    signal = parse_input()
    marker_index = None

    for index in range(3, len(signal)):
        signal_segment = signal[index-3:index+1]
        signal_segment_set = set(signal_segment)

        if len(signal_segment_set) == 4:
            marker_index = index + 1
            break

    print(marker_index)


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 6")
    part_1()
    part_2()
