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


def parse_strategy_guide():
    input_file = open("day_02/input", "r")
    rounds = []

    for line in input_file.readlines():
        split_line = line.rstrip().split(" ")
        rounds.append([opponent_map[split_line[0]], my_map[split_line[1]]])

    return rounds


def part_1():
    """
    What would your total score be if everything goes exactly according to your strategy guide?
    :return:
    """
    print("Part 1")
    rounds = parse_strategy_guide()
    total_points = 0

    for r in rounds:
        print(r[0], r[1])
        total_points += shape_points[r[1]]
        total_points += win_loss_draw_points[win_loss_draw_points_map[r[0] + r[1]]]

    print(total_points)


def part_2():
    """

    :return:
    """
    print("Part 2")
    pass


def go():
    print("Day 2")
    part_1()
    part_2()
