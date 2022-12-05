import re


def get_input() -> list[str]:
    with open('5/input.txt') as f:
        lines = f.readlines()
    return lines


def get_stacks(lines: list[str]) -> dict():
    lines.reverse()
    stacks = dict.fromkeys(list(range(1, 10)))
    for line in lines:
        for index in range(1, len(line), 4):
            if line[index] != ' ':
                if stacks[1+index//4] is None:
                    stacks[1+index//4] = []
                stacks[1+index//4].append(line[index])
    return stacks


def get_simplified_moves(lines: list[str]) -> list[int]:
    moves = []
    for line in lines:
        moves.append(list(map(int, re.findall(r'\d+', line))))
    return moves


def move_single(moves: list[int], stacks: dict()) -> dict():
    for move in moves:
        for _ in range(move[0]):
            in_transit = stacks[move[1]].pop()
            stacks[move[2]].append(in_transit)
    return stacks


def move_multiple(moves: list[int], stacks: dict()) -> dict:
    for move in moves:
        temp_stack = []
        for _ in range(move[0]):
            if len(stacks[move[1]]) > 0:
                in_transit = stacks[move[1]].pop()
                temp_stack.append(in_transit)
        temp_stack.reverse()
        stacks[move[2]].extend(temp_stack)
    return stacks


def run(part: int) -> str:
    if part != 1 and part != 2:
        print('Please enter valid part number')
        return None

    lines = get_input()
    moves_in = lines[10:]
    moves = get_simplified_moves(moves_in)
    stacks = get_stacks(lines[0:8])

    if part == 1:
        updated_stacks = move_single(moves, stacks)
    else:
        updated_stacks = move_multiple(moves, stacks)

    top_row = ''
    for stack in updated_stacks.values():
        top_crate = stack.pop()
        top_row += top_crate

    return top_row


if __name__ == '__main__':
    # Part 1
    top_row = run(1)
    print('The top row after all moves in part 1 looks like:\n', top_row)

    # Part 2
    top_row = run(2)
    print('The top row after all moves in part 2 looks like:\n', top_row)
