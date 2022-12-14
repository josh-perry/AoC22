import re
from enum import Enum


class Tile(Enum):
    AIR = 1,
    SAND = 2,
    WALL = 3


def resize_grid(grid, max_width, max_height):
    for y in range(len(grid), max_height):
        grid.append([])

    for y in range(0, max_height):
        for x in range(len(grid[y]), max_width):
            grid[y].append(Tile.AIR)


def parse_input():
    input_file = open("day_14/input", "r")
    grid = []

    grid_width = 0
    grid_height = 0

    line_segment_regex = r"(\d+),(\d+)"

    for line in input_file.readlines():
        line_segments = line.split(" -> ")

        current_x, current_y = None, None

        for line_segment in line_segments:
            positions = re.match(line_segment_regex, line_segment).groups()

            destination_x, destination_y = int(positions[0]), int(positions[1])

            grid_width = max(grid_width, destination_x + 1)
            grid_height = max(grid_height, destination_y + 1)
            resize_grid(grid, grid_width, grid_height)

            if current_x and current_y:
                grid[current_y][current_x] = Tile.WALL

            current_x = current_x or destination_x
            current_y = current_y or destination_y

            for x in range(current_x, destination_x, 1 if current_x < destination_x else -1):
                grid[destination_y][x] = Tile.WALL

            for y in range(current_y, destination_y, 1 if current_y < destination_y else -1):
                grid[y][destination_x] = Tile.WALL

            grid[destination_y][destination_x] = Tile.WALL

            current_x = destination_x
            current_y = destination_y

    return grid


def simulate_sand_fall(sand_origin_x, sand_origin_y, grid):
    sand_count = 0
    sand_x, sand_y = None, None

    while True:
        sand_x = sand_x or sand_origin_x
        sand_y = sand_y or sand_origin_y

        if sand_y + 1 >= len(grid):
            return sand_count

        if grid[sand_y + 1][sand_x] != Tile.AIR:
            if grid[sand_y + 1][sand_x - 1] == Tile.AIR:
                sand_x -= 1
            elif grid[sand_y + 1][sand_x + 1] == Tile.AIR:
                sand_x += 1
            else:
                grid[sand_y][sand_x] = Tile.SAND
                sand_count += 1

                sand_x = sand_origin_x
                sand_y = sand_origin_y
                continue

        sand_y = sand_y + 1


def part_1():
    """
    Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the
    abyss below?
    :return:
    """
    print("Part 1")
    grid = parse_input()

    settled_sand = simulate_sand_fall(500, 0, grid)
    print(settled_sand)


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            symbol = "."

            if grid[y][x] == Tile.WALL:
                symbol = "#"

            if grid[y][x] == Tile.SAND:
                symbol = "o"

            print(symbol, end="")

        print("")


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
