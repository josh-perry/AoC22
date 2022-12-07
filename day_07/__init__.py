import re
from dataclasses import dataclass


@dataclass
class FsNode:
    name: str
    children: dict
    parent: object
    size: int
    is_directory: bool


def calculate_directory_sizes(node):
    for child_index in node.children:
        child = node.children[child_index]

        if child.is_directory:
            calculate_directory_sizes(child)

        node.size += child.size


def find_nodes_smaller_than(node, smaller_than, nodes):
    nodes = (nodes if nodes is not None else [])

    for child_index in node.children:
        child = node.children[child_index]

        if child.is_directory:
            find_nodes_smaller_than(child, smaller_than, nodes)

        if node.size < smaller_than and node not in nodes:
            nodes.append(node)

    return nodes


def find_nodes_bigger_than(node, bigger_than, nodes):
    nodes = (nodes if nodes is not None else [])

    for child_index in node.children:
        child = node.children[child_index]

        if child.is_directory:
            find_nodes_bigger_than(child, bigger_than, nodes)

        if node.size > bigger_than and node not in nodes:
            nodes.append(node)

    return nodes


def parse_input():
    input_file = open("day_07/input", "r")
    command_regex = r"\$ (\w+) ?(.+)"
    file_regex = r"(\d+) (.+)"

    root_node = FsNode("/", {}, None, 0, True)
    current_node = root_node

    for line in input_file.readlines():
        match = re.match(command_regex, line)

        if match:
            groups = match.groups()
            command = groups[0]
            parameter = None

            if len(groups) > 1:
                parameter = groups[1]

            if command == "cd":
                if parameter == "/":
                    continue

                if parameter in current_node.children:
                    current_node = current_node.children[parameter]
                    continue

                if parameter == "..":
                    current_node = current_node.parent
                    continue

                current_node.children[parameter] = FsNode(parameter, {}, current_node, 0, True)
                current_node = current_node.children[parameter]

            continue

        file_match = re.match(file_regex, line)

        if file_match:
            groups = file_match.groups()
            filesize = int(groups[0])
            filename = groups[1]

            if filename not in current_node.children:
                current_node.children[filename] = FsNode(filename, None, current_node, filesize, False)

    calculate_directory_sizes(root_node)

    return root_node


def part_1():
    """
    Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those
    directories?
    :return:
    """
    print("Part 1")
    root_node = parse_input()

    nodes = find_nodes_smaller_than(root_node, 100001, [])

    total_size = sum(map(lambda x: x.size, nodes))
    print(total_size)


def part_2():
    """
    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What
    is the total size of that directory?
    :return:
    """
    print("Part 2")
    root_node = parse_input()

    total_space = 70000000
    space_required_for_update = 30000000
    current_free_space = total_space - root_node.size
    required_space_to_clear = abs(current_free_space - space_required_for_update)

    nodes = find_nodes_bigger_than(root_node, required_space_to_clear, [])

    smallest_size = min(map(lambda x: x.size, nodes))
    print(smallest_size)


def go():
    print("Day 7")
    part_1()
    part_2()
