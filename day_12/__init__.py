import collections
import math
from dataclasses import dataclass
from string import ascii_lowercase


class Node:
    x: int
    y: int
    elevation: int
    connecting_nodes: list

    def __init__(self, x, y, elevation):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.connecting_nodes = []

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class NodeGrid:
    nodes: list
    start_node_position: tuple
    end_node_position: tuple


def parse_input():
    input_file = open("day_12/input")
    nodes = []
    start_node_position = (0, 0)
    end_node_position = (0, 0)

    line_index = 0
    for line in input_file.readlines():
        row = []

        for character_index in range(0, len(line.rstrip())):
            character = line[character_index]

            if character == "S":
                elevation = 0
                end_node_position = (line_index, character_index)
            elif character == "E":
                elevation = ascii_lowercase.find("z")
                end_node_position = (line_index, character_index)
            else:
                elevation = ascii_lowercase.find(character)

            row.append(Node(line_index, character_index, elevation))

        nodes.append(row)
        line_index += 1

    return NodeGrid(nodes, start_node_position, end_node_position)


def calculate_connecting_nodes(node_grid):
    neighbour_offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for y in range(0, len(node_grid.nodes)):
        row = node_grid.nodes[y]
        pass

        for x in range(0, len(row)):
            node = row[x]

            for neighbour_offset in neighbour_offsets:
                if x + neighbour_offset[0] > len(row) - 1 or x + neighbour_offset[0] < 0:
                    continue

                if y + neighbour_offset[1] > len(node_grid.nodes) - 1 or y + neighbour_offset[1] < 0:
                    continue

                neighbour_node = node_grid.nodes[y + neighbour_offset[1]][x + neighbour_offset[0]]

                if neighbour_node.elevation <= node.elevation + 1:
                    node.connecting_nodes.append(neighbour_node)


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return not self.elements

    def add(self, element):
        self.elements.append(element)

    def get(self):
        return self.elements.popleft()


# thanks, redblob games
def pathfind(node_grid):
    x, y = node_grid.start_node_position[1], node_grid.start_node_position[0]
    starting_node = node_grid.nodes[y][x]

    x, y = node_grid.end_node_position[1], node_grid.end_node_position[0]
    destination_node = node_grid.nodes[y][x]

    node_queue = Queue()
    node_queue.add(starting_node)

    came_from = {starting_node: None}

    steps = 0

    while not node_queue.empty():
        current_node = node_queue.get()

        if current_node == destination_node:
            break

        for next_node in current_node.connecting_nodes:
            if next_node not in came_from:
                steps += 1
                came_from[next_node] = current_node
                node_queue.add(next_node)

    node = destination_node
    path = []

    while node is not starting_node:
        path.append(node)

        if node not in came_from:
            return None

        node = came_from[node]

    path.reverse()
    return path


def part_1():
    """
    What is the fewest steps required to move from your current position to the location that should get the best
    signal?
    :return:
    """
    print("Part 1")
    grid = parse_input()
    calculate_connecting_nodes(grid)
    path = pathfind(grid)

    print(len(path))


def part_2():
    """
    What is the fewest steps required to move starting from any square with elevation a to the location that should get
    the best signal?
    :return:
    """
    print("Part 2")
    grid = parse_input()
    calculate_connecting_nodes(grid)

    possible_starting_positions = []

    for y in range(0, len(grid.nodes)):
        row = grid.nodes[y]

        for x in range(0, len(row)):
            if grid.nodes[y][x].elevation == 0:
                possible_starting_positions.append((y, x))

    minimum_distance = math.inf

    for possible_starting_position in possible_starting_positions:
        grid.start_node_position = possible_starting_position
        path = pathfind(grid)

        if path:
            minimum_distance = min(len(path), minimum_distance)

    print(minimum_distance)


def go():
    print("Day 12")
    part_1()
    part_2()
