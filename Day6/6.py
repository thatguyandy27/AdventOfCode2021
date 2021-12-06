input = [1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 4, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 3, 3, 4, 1, 4, 1, 1, 3, 1, 1, 5, 1, 1, 1, 1, 4, 1, 1, 5, 1, 1, 1, 4, 1, 5, 1, 1, 1, 3, 1, 1, 5, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 2, 4, 1, 1, 1, 1, 4, 1, 2, 2, 1, 1, 1, 3, 1, 2, 5, 1, 4, 1, 1, 1, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 5, 1, 1, 1, 4, 1, 1, 5, 1, 1, 5, 3, 3, 5, 3, 1, 1,
         1, 4, 1, 1, 1, 1, 1, 1, 5, 3, 1, 2, 1, 1, 1, 4, 1, 3, 1, 5, 1, 1, 2, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4, 3, 2, 1, 2, 4, 1, 3, 1, 5, 1, 2, 1, 4, 1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 1, 1, 3, 1, 3, 3, 1, 4, 3, 4, 1, 1, 1, 1, 5, 1, 3, 3, 2, 5, 3, 1, 1, 3, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 1, 5, 1, 1, 1, 4, 4, 1, 1, 5, 5, 2, 4, 5, 1, 1, 1, 1, 5, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1]

new_num = 8
reset_num = 6


def getFishCounts(input):
    fishes = [0] * (new_num + 1)
    for i in input:
        fishes[i] += 1

    return fishes


def simDay(fishes):
    newFishes = [0] * (new_num + 1)

    # Move counters down
    for i in range(0, new_num):
        newFishes[i] = fishes[i + 1]

    # Move the zeros back to 7
    newFishes[reset_num] += fishes[0]

    # Create new fishes
    newFishes[8] = fishes[0]

    return newFishes


def runSim(input, days):
    fishes = getFishCounts(input)

    for d in range(days):
        fishes = simDay(fishes)
        # print(f'Day: {d}: ', fishes)

    return sum(fishes)


if __name__ == '__main__':
    # test = runSim([3, 4, 3, 1, 2], 80)
    # print(test)
    isPart1 = False
    if isPart1:
        total = runSim(input, 80)

        print('The answer is:', total)
    else:
        total = runSim(input, 256)

        print('The answer is:', total)
    # else:
    #     total = findWorstVents(filename, False)

    #     print('The answer is:', total)
