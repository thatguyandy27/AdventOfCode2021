filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day11/input.txt'
testfile = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day11/test.txt'


def parseInput(filename):
    nums = []

    with open(filename) as f:
        for line in f:
            row = []
            for i in range(len(line) - 1):
                row.append(int(line[i]))

            nums.append(row)

    return nums


def performFlash(grid, i, j):
    if grid[i][j] <= 9:
        return 0

    # print(f'flashing at {i}, {j}')
    flashes = 1
    grid[i][j] = 0

    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            # Ignore 0s as they have been reset
            if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[0]) and grid[ii][jj] > 0:
                grid[ii][jj] += 1
                flashes += performFlash(grid, ii, jj)

    return flashes


def performFlashes(grid):
    flashes = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            flashes += performFlash(grid, i, j)

    return flashes


def performStepAndCountFlashes(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

    return performFlashes(grid)


def countFlashes(grid, steps):
    flashes = 0
    for i in range(steps):
        flashes += performStepAndCountFlashes(grid)
        # print(grid)
    return flashes


def findAllFlashes(grid):
    expected = len(grid) * len(grid[0])
    found = 0
    step = 0
    while expected != found:
        step += 1
        found = performStepAndCountFlashes(grid)

    return step


if __name__ == '__main__':
    isPart1 = False
    # nums = parseInput(testfile)
    nums = parseInput(filename)
    if isPart1:
        total = countFlashes(nums, 100)
        print('The answer is:', total)
    else:
        total = findAllFlashes(nums)
        print('The answer is:', total)
