filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day10/input.txt'


def parseInput(filename):
    lines = []

    with open(filename) as f:
        for line in f:
            lines.append(line)
    return lines


def getPoints(line):
    map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []

    for c in line:
        if c == '{' or c == '(' or c == '<' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            l = stack.pop()
            if (c == ')' and l != '(') or \
                    (c == '}' and l != '{') or \
                    (c == ']' and l != '[') or \
                    (c == '>' and l != '<'):
                return map[c]
    return 0


def getPointsForCorruptedLines(lines):
    pts = 0
    count = 0
    for line in lines:
        pt = getPoints(line)
        if pt > 0:
            count += 1
        pts += pt

    print(count)
    return pts


def getAutoCompleteScore(line):
    stack = []

    for c in line:
        if c == '\n':
            continue
        if c == '{' or c == '(' or c == '<' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            l = stack.pop()
            if (c == ')' and l != '(') or \
                    (c == '}' and l != '{') or \
                    (c == ']' and l != '[') or \
                    (c == '>' and l != '<'):
                return 0

    missingVal = {
        '<': 4,
        '{': 3,
        '[': 2,
        '(': 1
    }
    currentScore = 0

    # we have leftovers
    while len(stack) > 0:
        l = stack.pop()
        currentScore *= 5
        currentScore += missingVal[l]

    return currentScore


def getMiddleScoreForAutocomplete(lines):
    scores = []

    for line in lines:
        score = getAutoCompleteScore(line)
        if score > 0:
            scores.append(score)

    scores = sorted(scores)
    print(len(scores))
    idx = (len(scores) // 2)
    print(idx)
    return scores[idx]


test_lines = ['[({(<(())[]>[[{[]{<()<>>',
              '[(()[<>])]({[<{<<[]>>(',
              '{([(<{}[<>[]}>{[]{[(<()>',
              '(((({<>}<{<{<>}{[]{[]{}',
              '[[<[([]))<([[{}[[()]]]',
              '[{[{({}]{}}([{[{{{}}([]',
              '{<[[]]>}<{[{[{[]{()[[[]',
              '[<(<(<(<{}))><([]([]()',
              '<{([([[(<>()){}]>(<<{{',
              '<{([{{}}[<[[[<>{}]]]>[]]']

if __name__ == '__main__':
    isPart1 = False
    lines = parseInput(filename)

    if isPart1:
        total = getPointsForCorruptedLines(lines)
        print('The answer is:', total)
    else:
        total = getMiddleScoreForAutocomplete(lines)
        print('The answer is:', total)
