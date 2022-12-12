from collections import defaultdict

MILLION = 1000000


def get_input() -> list[str]:
    with open('7/input.txt') as f:
        lines = f.readlines()
    return lines


def get_sums_of_dirs(lines: list[str]) -> dict():
    sums = defaultdict(int)
    pwd = []

    for line in lines:
        match line.strip().split():
            case ['$', 'ls']:
                pass
            case ['$', 'cd', path]:
                if path == '..':
                    pwd.pop()
                elif path == '/':
                    pwd = []
                else:
                    pwd.append(path)
            case ['dir', _]:
                pass
            case [size, _]:
                for index in range(0, len(pwd)):
                    folder_name = '/'.join(pwd[0: index+1])
                    sums[folder_name] += int(size)

    return sums


def get_sums_of_small_dirs(sums: dict(), max_val: int = 100000) -> int:
    result = 0
    for val in sums.values():
        if val <= max_val:
            result += val

    return result


def find_min_dir_with_constraint(sums: dict(), max_space: int = 70*MILLION, min_space: int = 30*MILLION) -> int:
    current_space = max_space - 43788975
    space_to_free = min_space-current_space

    return (min(filter(lambda x: space_to_free <= x, sums.values())))


if __name__ == '__main__':
    lines = get_input()

    # Part 1
    sums = get_sums_of_dirs(lines)
    sums_of_small = get_sums_of_small_dirs(sums)
    print('The result for part 1 is:', sums_of_small)

    # Part 2
    min_dir_size = find_min_dir_with_constraint(sums)
    print('The result for part 2 is:', min_dir_size)
