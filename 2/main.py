# Rock:     A & X   1p
# Paper:    B & Y   2p
# Scissors: C & Z   3p

# Win:              6p
# Draw:             3p
# Loss:             0p

# For part 2:
# X - lose
# Y - draw
# Z - win


POINT_TRANSLATION_1 = {'A X': 4,
                       'A Y': 8,
                       'A Z': 3,
                       'B X': 1,
                       'B Y': 5,
                       'B Z': 9,
                       'C X': 7,
                       'C Y': 2,
                       'C Z': 6, }

POINT_TRANSLATION_2 = {'A X': 3,
                       'A Y': 4,
                       'A Z': 8,
                       'B X': 1,
                       'B Y': 5,
                       'B Z': 9,
                       'C X': 2,
                       'C Y': 6,
                       'C Z': 7, }


def get_input():
    with open('2/input.txt') as f:
        lines = f.readlines()
    return lines


def calculate_points(lines: list[str], point_translation: dict()):
    points = 0
    for line in lines:
        points += point_translation[line.strip()]

    return points


if __name__ == '__main__':
    lines = get_input()

    # Part 1
    points_1 = calculate_points(lines, POINT_TRANSLATION_1)
    print('Points in part 1: ', points_1)

    # Part 2
    points_2 = calculate_points(lines, POINT_TRANSLATION_2)
    print('Points in part 2: ', points_2)
