import re
from enum import Enum


class Operation(Enum):
    ADD = 1,
    SUB = 2,
    MUL = 3
    DIV = 4


class Monkey:
    items = []
    operation_symbol: Operation
    operation_value: int
    operation_self_value: bool
    test_divisible_by: int
    true_monkey: int
    false_monkey: int


def parse_input():
    input_file = open("day_11/input", "r")

    monkey_start_regex = r"Monkey (\d+):"
    starting_items_regex = r"  Starting items: (.+)"
    operation_regex = r"  Operation: new = old (\+|\*|\/|\-) (.+)"
    test_regex = r"  Test: divisible by (\d+)"
    if_true_regex = r"    If true: throw to monkey (\d+)"
    if_false_regex = r"    If false: throw to monkey (\d+)"

    monkeys = []
    current_monkey = None

    for line in input_file.readlines():
        monkey_start_match = re.match(monkey_start_regex, line)
        if monkey_start_match:
            if current_monkey:
                monkeys.append(current_monkey)

            current_monkey = Monkey()
            continue

        starting_items_match = re.match(starting_items_regex, line, )
        if starting_items_match:
            starting_items_list = starting_items_match.groups()[0].split(",")
            current_monkey.items = list(map(lambda x: int(x), starting_items_list))
            continue

        operation_match = re.match(operation_regex, line)
        if operation_match:
            operation_match_groups = operation_match.groups()

            if operation_match_groups[0] == "+":
                current_monkey.operation_symbol = Operation.ADD
            elif operation_match_groups[0] == "-":
                current_monkey.operation_symbol = Operation.SUB
            elif operation_match_groups[0] == "/":
                current_monkey.operation_symbol = Operation.DIV
            elif operation_match_groups[0] == "*":
                current_monkey.operation_symbol = Operation.MUL

            value = operation_match_groups[1]

            if value == "old":
                current_monkey.operation_value = None
                continue

            current_monkey.operation_value = int(operation_match_groups[1])
            continue

        test_regex_match = re.match(test_regex, line)
        if test_regex_match:
            current_monkey.test_divisible_by = int(test_regex_match.groups()[0])
            continue

        if_true_match = re.match(if_true_regex, line)
        if if_true_match:
            current_monkey.true_monkey = int(if_true_match.groups()[0])
            continue

        if_false_match = re.match(if_false_regex, line)
        if if_false_match:
            current_monkey.false_monkey = int(if_false_match.groups()[0])
            continue

    monkeys.append(current_monkey)
    return monkeys


def simulate_monkey_business(monkeys, max_rounds):
    monkey_inspection_counts = []

    for r in range(0, max_rounds):
        for monkey_index in range(0, len(monkeys)):
            monkey = monkeys[monkey_index]

            if len(monkey_inspection_counts) < monkey_index + 1:
                monkey_inspection_counts.append(0)

            for item_number in range(0, len(monkey.items)):
                item = monkey.items.pop(0)
                monkey_inspection_counts[monkey_index] += 1
                operation_value = monkey.operation_value or item

                if monkey.operation_symbol == Operation.MUL:
                    item *= operation_value
                elif monkey.operation_symbol == Operation.DIV:
                    item //= operation_value
                elif monkey.operation_symbol == Operation.ADD:
                    item += operation_value
                elif monkey.operation_symbol == Operation.SUB:
                    item -= operation_value

                item = item // 3

                if item % monkey.test_divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(item)
                else:
                    monkeys[monkey.false_monkey].items.append(item)

    return monkey_inspection_counts


def part_1():
    """
    Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of
    monkey business after 20 rounds of stuff-slinging simian shenanigans?
    :return:
    """
    print("Part 1")
    monkeys = parse_input()

    monkey_inspection_counts = simulate_monkey_business(monkeys, 20)
    top_inspection_counts = sorted(monkey_inspection_counts, reverse=True)[:2]

    monkey_business = 1
    for inspection_counts in top_inspection_counts:
        monkey_business *= inspection_counts

    print(monkey_business)

def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 11")
    part_1()
    part_2()
