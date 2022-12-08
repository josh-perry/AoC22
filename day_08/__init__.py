from dataclasses import dataclass


def parse_input():
    input_file = open("day_08/input", "r")
    grid = []

    for line in input_file.readlines():
        row = []

        for tree_index in range(0, len(line.rstrip())):
            tree = line[tree_index]
            row.append(int(tree))

        grid.append(row)

    return grid


def count_visible_trees_from_outside(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)

    @dataclass
    class VisibilityLine:
        starting_x: int
        starting_y: int
        offset_x: int
        offset_y: int

    visibility_lines = []

    for x in range(0, grid_width):
        visibility_lines.append(VisibilityLine(x, 0, 0, 1))
        visibility_lines.append(VisibilityLine(x, grid_height - 1, 0, -1))

    for y in range(0, grid_height):
        visibility_lines.append(VisibilityLine(0, y, 1, 0))
        visibility_lines.append(VisibilityLine(grid_height - 1, y, -1, 0))

    visible_trees = []

    for line in visibility_lines:
        biggest_tree_seen = -1

        grid_x = line.starting_x
        grid_y = line.starting_y

        while grid_width > grid_x >= 0 and grid_height > grid_y >= 0:
            tree = grid[grid_y][grid_x]

            if grid_x == line.starting_x and grid_y == line.starting_y:
                visible_trees.append((grid_y, grid_x))
            elif tree > biggest_tree_seen:
                visible_trees.append((grid_y, grid_x))

            biggest_tree_seen = max(biggest_tree_seen, tree)

            grid_x += line.offset_x
            grid_y += line.offset_y

    return len(set(visible_trees))


def part_1():
    """
    Consider your map; how many trees are visible from outside the grid?
    :return:
    """
    print("Part 1")
    grid = parse_input()
    visible_trees = count_visible_trees_from_outside(grid)

    print(visible_trees)


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 8")
    part_1()
    part_2()
