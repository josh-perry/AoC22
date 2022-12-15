import re
from dataclasses import dataclass


@dataclass
class SensorResult:
    position: tuple
    beacon_position: tuple

    def __init__(self, sensor_position, beacon_position):
        self.position = sensor_position
        self.beacon_position = beacon_position
        self.distance = abs(sensor_position[0] - beacon_position[0]) + abs(sensor_position[1] - beacon_position[1])


def parse_input():
    input_file = open("day_15/input")
    sensor_regex = r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)"
    sensor_results = []

    for line in input_file:
        sensor_regex_match_groups = re.match(sensor_regex, line).groups()

        sensor_position = (int(sensor_regex_match_groups[0]), int(sensor_regex_match_groups[1]))
        beacon_position = (int(sensor_regex_match_groups[2]), int(sensor_regex_match_groups[3]))
        sensor_results.append(SensorResult(sensor_position, beacon_position))

    return sensor_results


def find_positions_with_no_beacon_for_row(sensor_results, y):
    confirmed_beacons = set()
    impossible_beacons = set()

    for sensor in sensor_results:
        sensor_x, sensor_y = sensor.position[0], sensor.position[1]
        beacon_x, beacon_y = sensor.beacon_position[0], sensor.beacon_position[1]

        if beacon_y == y:
            confirmed_beacons.add(sensor.beacon_position)

        if sensor_y - sensor.distance <= y <= sensor_y + sensor.distance:
            leftmost = sensor_x + abs(y - sensor_y) - sensor.distance
            rightmost = sensor_x - abs(y - sensor_y) + sensor.distance
            impossible_beacons.update([(x, y) for x in range(leftmost, rightmost + 1)])

    return len(impossible_beacons) - len(confirmed_beacons)


def part_1():
    """
    Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain
    a beacon?
    :return:
    """
    print("Part 1")
    sensor_results = parse_input()

    print(find_positions_with_no_beacon_for_row(sensor_results, 2000000))


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 15")
    part_1()
    part_2()
