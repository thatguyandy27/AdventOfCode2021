board_max = 1000
filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day5/input.txt'


def parsePt(pt):
    x, y = pt.split(',')
    return int(x), int(y)


def parseLines(filename, filterDiagonal):
    lines = []
    with open(filename) as f:
        for line in f:
            pts = line.split(' -> ')
            x1, y1 = parsePt(pts[0])
            x2, y2 = parsePt(pts[1])

            if filterDiagonal:
                if x1 == x2 or y1 == y2:
                    lines.append([(x1, y1), (x2, y2)])
            else:
                lines.append([(x1, y1), (x2, y2)])

    return lines


def createBoard(size):
    return [[0 for i in range(size)] for j in range(size)]


def markVertical(board, x, y1, y2):
    for i in range(y1, y2 + 1):
        board[i][x] += 1
    return board


def markHorizontal(board, y, x1, x2):
    for i in range(x1, x2 + 1):
        board[y][i] += 1
    return board


def markDiagonal(board, x1, y1, x2, y2):
    dir = 1 if x1 < x2 else -1
    xDiff = list(range(x1, x2 + dir, dir))
    dir = 1 if y1 < y2 else -1
    yDiff = list(range(y1, y2 + dir, dir))

    for i in range(len(xDiff)):
        x = xDiff[i]
        y = yDiff[i]
        board[y][x] += 1
    return board


def markBoard(board, line):
    pt1 = line[0]
    pt2 = line[1]

    if pt1[1] == pt2[1]:
        x1 = min(pt1[0], pt2[0])
        x2 = max(pt1[0], pt2[0])
        y = pt1[1]
        board = markHorizontal(board, y, x1, x2)
    elif pt1[0] == pt2[0]:
        y1 = min(pt1[1], pt2[1])
        y2 = max(pt1[1], pt2[1])
        x = pt1[0]
        board = markVertical(board, x, y1, y2)
    else:
        board = markDiagonal(board, pt1[0], pt1[1],  pt2[0], pt2[1])

    return board


def countDanger(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 1:
                total += 1
    return total


def findWorstVents(filename, filterDiagonal):
    lines = parseLines(filename, filterDiagonal)
    board = createBoard(board_max)

    for line in lines:
        board = markBoard(board, line)

    return countDanger(board)


if __name__ == '__main__':
    isPart1 = False
    if isPart1:
        total = findWorstVents(filename, True)

        print('The answer is:', total)
    else:
        total = findWorstVents(filename, False)

        print('The answer is:', total)
