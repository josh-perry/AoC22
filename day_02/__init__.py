shape_points = {
    'R': 1,
    'P': 2,
    'S': 3
}


opponent_map = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}


my_map = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}


win_loss_draw_points = {
    'win': 6,
    'draw': 3,
    'loss': 0
}


win_loss_draw_points_map = {
    'RR': 'draw',
    'RP': 'win',
    'RS': 'loss',
    'PP': 'draw',
    'PR': 'loss',
    'PS': 'win',
    'SS': 'draw',
    'SR': 'win',
    'SP': 'loss'
}


move_intention_outcome_map = {
    'RX': 'S',
    'RY': 'R',
    'RZ': 'P',
    'PX': 'R',
    'PY': 'P',
    'PZ': 'S',
    'SX': 'P',
    'SY': 'S',
    'SZ': 'R'
}

def parse_strategy_guide_part_1():
    input_file = open("day_02/input", "r")
    rounds = []

    for line in input_file.readlines():
        split_line = line.rstrip().split(" ")
        rounds.append([opponent_map[split_line[0]], my_map[split_line[1]]])

    return rounds


def parse_strategy_guide_part_2():
    input_file = open("day_02/input", "r")
    rounds = []

    for line in input_file.readlines():
        split_line = line.rstrip().split(" ")

        first_move = split_line[0]
        second_move = move_intention_outcome_map[opponent_map[split_line[0]] + split_line[1]]

        rounds.append([opponent_map[first_move], second_move])

    return rounds


def calculate_points(rounds):
    total_points = 0

    for r in rounds:
        total_points += shape_points[r[1]]
        total_points += win_loss_draw_points[win_loss_draw_points_map[r[0] + r[1]]]

    return total_points


def part_1():
    """
    What would your total score be if everything goes exactly according to your strategy guide?
    :return:
    """
    print("Part 1")
    rounds = parse_strategy_guide_part_1()
    total_points = calculate_points(rounds)
    print(total_points)


def part_2():
    """
    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
    according to your strategy guide?
    :return:
    """
    print("Part 2")
    rounds = parse_strategy_guide_part_2()
    total_points = calculate_points(rounds)
    print(total_points)


def go():
    print("Day 2")
    part_1()
    part_2()
