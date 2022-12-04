

def part_1():
    with open('1/input.txt') as f:
        lines = f.readlines()

    sums = []
    index = 0
    for line in lines:
        if line.strip() == '':
            index += 1

        if len(sums) == index:
            sums.append(0)
        else:
            sums[index] += int(line)

    print('Maximum calories: ', max(sums))

    return sums


def part_2(arr: list, n: int):
    top_sum = sum(sorted(arr, reverse=True)[:n])
    print('The top {} elves are carrying a total of {} calories.'.format(n, top_sum))


if __name__ == '__main__':
    sums = part_1()
    part_2(sums, 3)
