filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day1/input.txt'


def countAscending(data):
    curr = data[0]
    count = 0
    for d in data:
        if d > curr:
            count += 1
        curr = d

    return count


def countAscendingWindow(data):
    window = sum(data[:3])
    count = 0
    for i in range(2, len(data)):
        newWindow = window + data[i] - data[i - 3]
        if newWindow > window:
            count += 1
        window = newWindow

    return count


if __name__ == '__main__':
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(int(line))

    # Part A:
    # print('The answer is:', countAscending(lines))
    # Part B:
    print('The answer is:', countAscendingWindow(lines))
