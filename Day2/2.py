filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day2/input.txt'


def parseLine(line):
    dir, amt = line.split(' ')
    return (dir, int(amt))


def getPosition(cmds):
    xPos = 0
    yPos = 0

    for dir, amt in cmds:
        if dir == 'forward':
            xPos += amt
        elif dir == 'down':
            yPos += amt
        elif dir == 'up':
            yPos -= amt
    return (xPos, yPos)


def getPosition2(cmds):
    xPos = 0
    yPos = 0
    aim = 0

    for dir, amt in cmds:
        if dir == 'forward':
            xPos += amt
            yPos += (aim * amt)
        elif dir == 'down':
            aim += amt
        elif dir == 'up':
            aim -= amt
    return (xPos, yPos)


if __name__ == '__main__':
    isPart1 = False
    cmds = []
    with open(filename) as f:
        for line in f:
            cmds.append(parseLine(line))

    if isPart1:
        xPos, yPos = getPosition(cmds)

        print('The answer is:', xPos * yPos)
    else:
        xPos, yPos = getPosition2(cmds)

        print('The answer is:', xPos * yPos)
