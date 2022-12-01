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


"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
def part_1():
    print("Part 1")
    elves = parse_elves()

    most_calories = -1

    for elf in elves:
        most_calories = max(most_calories, sum(elf.food))

    print(most_calories)



def go():
    print("Day 1")
    part_1()
