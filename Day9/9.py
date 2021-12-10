filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day9/input.txt'


def parseInput(filename):
    nums = []

    with open(filename) as f:
        for line in f:
            row = []
            for i in range(len(line) - 1):
                row.append(int(line[i]))

            nums.append(row)

    return nums


def getNumSafe(nums, i, j):
    if i >= 0 and j >= 0 and i < len(nums) and j < len(nums[0]):
        return nums[i][j]
    return 10


def findLowpoints(nums):
    total = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            pt = nums[i][j]
            if pt < getNumSafe(nums, i - 1, j) and pt < getNumSafe(nums, i + 1, j) and \
                    pt < getNumSafe(nums, i, j - 1) and pt < getNumSafe(nums, i, j + 1):
                total += pt + 1

    return total


def findBasin(nums, pt):
    included = set()
    queue = [pt]
    size = 0
    while len(queue) > 0:
        (i, j) = queue.pop(0)
        pt = getNumSafe(nums, i, j)
        if pt >= 9 or (i, j) in included:
            continue

        # if (pt < getNumSafe(nums, i - 1, j) or (i - 1, j) in included) and \
        #     (pt < getNumSafe(nums, i + 1, j) or (i + 1, j) in included) and \
        #     (pt < getNumSafe(nums, i, j - 1) or (i, j - 1) in included) and \
        #         (pt < getNumSafe(nums, i, j + 1) or (i, j + 1) in included):
        size += 1
        included.add((i, j))

        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))

    return size


def part2(nums):
    basins = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            pt = nums[i][j]
            if pt < getNumSafe(nums, i - 1, j) and pt < getNumSafe(nums, i + 1, j) and \
                    pt < getNumSafe(nums, i, j - 1) and pt < getNumSafe(nums, i, j + 1):
                basinSize = findBasin(nums, (i, j))

                print(f'is basin: ({i}, {j}): {pt}, size: {basinSize}')
                basins.append(basinSize)

    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]


test_nums = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
             [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
             [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

if __name__ == '__main__':
    isPart1 = False
    if isPart1:
        nums = parseInput(filename)
        total = findLowpoints(nums)
        print('The answer is:', total)
    else:
        nums = parseInput(filename)
        total = part2(nums)
        print('The answer is:', total)
