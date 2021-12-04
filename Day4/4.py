called_numbers = [62, 55, 98, 93, 48, 28, 82, 78, 19, 96, 31, 42, 76, 25, 34, 4, 18, 80, 66, 6, 14, 17, 57, 54, 90, 27, 40, 47, 9, 36, 97, 56, 87, 61, 91, 1, 64, 71, 99, 38, 70, 5, 94, 85, 49, 59, 69, 26,
                  21, 60, 0, 79, 2, 95, 11, 84, 20, 24, 8, 51, 46, 44, 88, 22, 16, 53, 7, 32, 89, 67, 15, 86, 41, 92, 10, 77, 68, 63, 43, 75, 33, 30, 81, 37, 83, 3, 39, 65, 12, 45, 23, 73, 72, 29, 52, 58, 35, 50, 13, 74]

filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day4/boards.txt'


def parseBoards(file):
    boards = []

    with open(filename) as f:
        board = []
        l = 0
        for line in f:
            if line == '' or l == 5:
                boards.append(board)
                board = []
                l = 0
            else:
                row = []
                cursor = 0
                for i in range(5):
                    row.append(int(line[cursor:cursor + 2]))
                    cursor = cursor + 3
                board.append(row)
                l += 1

    boards.append(board)
    print(boards[-1])
    return boards


def createMarkedBoard():
    return [[False for i in range(5)] for j in range(5)]


def isWinner(marked):
    for i in range(5):
        found = True
        for j in range(5):
            if not marked[i][j]:
                found = False
                break
        if found:
            return found

    for j in range(5):
        found = True
        for i in range(5):
            if not marked[i][j]:
                found = False
                break
        if found:
            return found

    return False


def getScore(board, marked):
    total = 0
    for i in range(5):
        for j in range(5):
            if not marked[i][j]:
                total += board[i][j]

    return total


def markAndCheckBoard(board, marked, nextNum):
    for i in range(5):
        for j in range(5):
            if board[i][j] == nextNum:
                marked[i][j] = True
                return isWinner(marked)

    return False


def findWorstBoard(file):
    boards = parseBoards(file)
    markedBoards = [createMarkedBoard() for i in range(len(boards))]
    finishedBoards = [False for i in range(len(boards))]
    boardsLeft = len(boards)
    for num in called_numbers:
        for i in range(len(boards)):

            if not finishedBoards[i]:
                board = boards[i]
                markedBoard = markedBoards[i]
                isWinner = markAndCheckBoard(board, markedBoard, num)
                if isWinner:
                    finishedBoards[i] = True
                    boardsLeft -= 1
                    if boardsLeft == 0:
                        score = getScore(board, markedBoard)
                        return score * num


def findBestBoard(file):
    boards = parseBoards(file)
    markedBoards = [createMarkedBoard() for i in range(len(boards))]

    for num in called_numbers:
        # print(num)
        for i in range(len(boards)):

            board = boards[i]
            markedBoard = markedBoards[i]
            isWinner = markAndCheckBoard(board, markedBoard, num)
            if isWinner:
                score = getScore(board, markedBoard)
                return score * num

    return "FAIL"


if __name__ == '__main__':
    isPart1 = False
    if isPart1:
        best = findBestBoard(filename)

        print('The answer is:', best)
    else:
        worst = findWorstBoard(filename)
        print('The answer is:', worst)
