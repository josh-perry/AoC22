class Elf:
    def __init__(self):
        self.food = []


def parse_elves():
    input_file = open("day_01/input", "r")
    elves = []
    elf = Elf()

    for line in input_file.readlines():
        if line.isspace():
            elves.append(elf)
            elf = Elf()
            continue

        elf.food.append(int(line))

    return elves


def part_1():
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    :return:
    """
    print("Part 1")
    elves = parse_elves()

    most_calories = -1

    for elf in elves:
        most_calories = max(most_calories, sum(elf.food))

    print(most_calories)


def part_2():
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    :return:
    """
    print("Part 2")
    elves = parse_elves()
    elves.sort(reverse=True, key=lambda x: sum(x.food))

    foods = list(map(lambda x: sum(x.food), elves[0:3]))
    print(sum(foods))


def go():
    print("Day 1")
    part_1()
    part_2()
