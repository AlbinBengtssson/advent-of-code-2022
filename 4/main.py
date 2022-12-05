def get_input() -> str:
    with open('4/input.txt') as f:
        lines = f.readlines()
    return lines


def eval_part_1(low_0, high_0, low_1, high_1):
    if (int(low_0) >= int(low_1) and int(high_0) <= int(high_1)) or (int(low_1) >= int(low_0) and int(high_1) <= int(high_0)):
        return True

    return False


def eval_part_2(low_0, high_0, low_1, high_1):
    if (int(low_0) <= int(low_1) and int(low_1) <= int(high_0)) or (int(low_1) <= int(low_0) and int(low_0) <= int(high_1)):
        return True

    return False


def check_duplicate_work(lines: str, part: int):

    if part != 1 and part != 2:
        print('Give valid input for part')
        return None

    res = 0
    for line in lines:
        pair = line.replace('\n', '').split(',')
        low_0, high_0 = pair[0].split('-')
        low_1, high_1 = pair[1].split('-')

        if part == 1 and eval_part_1(low_0, high_0, low_1, high_1):
            res += 1
        elif part == 2 and eval_part_2(low_0, high_0, low_1, high_1):
            res += 1

    return res


if __name__ == '__main__':
    lines = get_input()

    # Part 1
    res_1 = check_duplicate_work(lines, 1)
    print('The result for part 1 is: ', res_1)

    # Part 2
    res_2 = check_duplicate_work(lines, 2)
    print('The result for part 2 is: ', res_2)
