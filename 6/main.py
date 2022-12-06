def get_input() -> str:
    with open('6/input.txt') as f:
        line = f.readlines()
    return str(line[0])


def find_package_start(input: str, packet_length: int) -> int:
    index = 0
    for index in range(0, len(input)-packet_length):
        x = set(filter(lambda x: input[index:index +
                                       packet_length].count(x) > 1, input))

        if not x:
            return index + packet_length
        index += 1


if __name__ == '__main__':
    input = get_input()

    # Part 1
    first_start = find_package_start(input, 4)
    print('First start of packet occurs on: ', first_start)

    # Part 2
    message_start = find_package_start(input, 14)
    print('First start of message occurs on: ', message_start)
