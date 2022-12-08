from dataclasses import dataclass


@dataclass
class VisibilityLine:
    starting_x: int
    starting_y: int
    offset_x: int
    offset_y: int


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


def calculate_viewing_distances_for_grid(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)

    viewing_distances_grid = []
    visibility_lines = []

    for y in range(0, grid_height):
        row = []

        for x in range(0, grid_width):
            row.append([])

            visibility_lines.append(VisibilityLine(x, y, 0, 1))
            visibility_lines.append(VisibilityLine(x, y, 0, -1))
            visibility_lines.append(VisibilityLine(x, y, -1, 0))
            visibility_lines.append(VisibilityLine(x, y, 1, 0))

        viewing_distances_grid.append(row)

    for line in visibility_lines:
        grid_x = line.starting_x
        grid_y = line.starting_y

        starting_tree = grid[line.starting_y][line.starting_x]
        viewing_distance = 0

        while grid_width > grid_x + line.offset_x >= 0 and grid_height > grid_y + line.offset_y >= 0:
            grid_x += line.offset_x
            grid_y += line.offset_y
            tree = grid[grid_y][grid_x]

            viewing_distance += 1

            if tree >= starting_tree:
                break

        viewing_distances_grid[line.starting_y][line.starting_x].append(viewing_distance)

    return viewing_distances_grid


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
    Consider each tree on your map. What is the highest scenic score possible for any tree?
    :return:
    """
    print("Part 2")
    grid = parse_input()
    viewing_distances = calculate_viewing_distances_for_grid(grid)
    max_scenic_score = -1

    grid_width = len(grid[0])
    grid_height = len(grid)

    for y in range(0, grid_height):
        for x in range(0, grid_width):
            score = 1

            for distance in viewing_distances[y][x]:
                score *= distance

            max_scenic_score = max(max_scenic_score, score)

    print(max_scenic_score)


def go():
    print("Day 8")
    part_1()
    part_2()
