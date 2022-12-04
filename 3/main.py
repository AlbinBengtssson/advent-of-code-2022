import string


def get_input() -> str:
    with open('3/input.txt') as f:
        lines = f.readlines()
    return lines


def get_compartments(line: str) -> list[str]:
    comp_1, comp_2 = line[:len(line)//2], line[len(line)//2:]
    return comp_1, comp_2


def get_priority_dict() -> dict():
    priorities = {}
    for index, s in enumerate(string.ascii_letters):
        priorities[s] = index+1

    return priorities


def get_match(comp_1: str, comp_2: str) -> str:
    return list(set(comp_1) & set(comp_2))[0]


def generate_groups(lines: str, chunk_size: int = 3):
    for i in range(0, len(lines), chunk_size):
        yield lines[i:i + chunk_size]


def part_1(lines: list[str], priorities: dict()) -> int:
    sum = 0
    for line in lines:
        comp_1, comp_2 = get_compartments(line)
        match = get_match(comp_1, comp_2)
        sum += priorities[match]

    return sum


def find_match(group: list[str]) -> str:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            return char


def part_2(groups: list[str], priorities: dict()) -> int:
    sum = 0
    for group in groups:
        match = find_match(group)
        sum += priorities[match]
    return sum


if __name__ == '__main__':
    lines = get_input()
    priorities = get_priority_dict()

    # Part 1
    sum_1 = part_1(lines, priorities)
    print('The sum of the priorities for part 1 is: ', sum_1)

    # Part 2
    groups = list(generate_groups(lines))
    sum_2 = part_2(groups, priorities)
    print('The sum of the priorities for part 2 is: ', sum_2)
