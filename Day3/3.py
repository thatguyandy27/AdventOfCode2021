filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day3/input.txt'


def parseFile(filename):
    # 010000010010
    sums = [[], [], [], [], [], [], [], [], [], [], [], []]

    with open(filename) as f:
        for line in f:
            for i in range(len(line) - 1):
                sums[i].append(int(line[i]))

    result = []
    for s in sums:
        result.append(sum(s))

    return result, len(sums[0])


def parseFileAsIntegers(filename):
    nums = []
    with open(filename) as f:
        for line in f:
            nums.append(int(line, 2))

    return nums


def part1(filename):
    result, length = parseFile(filename)

    gamma = ''
    epsilon = ''
    for res in result:
        if res > length // 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    g = int(gamma, 2)
    e = int(epsilon, 2)

    return e * g


def part2(filename):
    max_bits = 12
    nums = parseFileAsIntegers(filename)

    oxygen = nums
    cursor = max_bits - 1
    while len(oxygen) > 1:
        oxygen = filterNums(oxygen, cursor, True)
        cursor -= 1

    co2 = nums
    cursor = max_bits - 1
    while len(co2) > 1:
        co2 = filterNums(co2, cursor, False)
        cursor -= 1

    return co2[0] * oxygen[0]


def filterNums(nums, bitPos, mostCommon):
    ones = []
    zeros = []
    mask = 1 << bitPos
    for num in nums:
        if num & mask > 0:
            ones.append(num)
        else:
            zeros.append(num)

    if mostCommon:
        if len(ones) >= len(zeros):
            return ones
        else:
            return zeros
    else:
        if len(ones) < len(zeros):
            return ones
        else:
            return zeros


if __name__ == '__main__':
    # res = part1(filename)
    # print(res)
    res = part2(filename)
    print(res)
