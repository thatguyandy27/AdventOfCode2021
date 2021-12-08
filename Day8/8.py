filename = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day8/input.txt'
test = '/Users/andrew.meyers/Documents/andy/AdventOfCode2021/Day8/test.txt'


def parseInput(filename):
    left = []
    right = []

    with open(filename) as f:
        for line in f:
            line = line.replace('\n', '')
            d = line.split(' | ')
            left.append(d[0].split(' '))
            right.append(d[1].split(' '))

    return left, right


def countUnique(filename):
    left, right = parseInput(filename)

    counts = [0] * 8

    for r in right:
        for digit in r:
            counts[len(digit)] += 1

    return counts[2] + counts[3] + counts[4] + counts[7]


def baseMap():
    return {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9
    }

# # Attempts to decode the right


# def decode5(charMap, digit):
#     isTwo = True
#     isFive = True
#     isThree = True
#     # do we know BCEF?
#     if 'b' in charMap:
#         bChar = charMap['b']
#         if bChar in digit:
#             isThree = False
#             isTwo = False
#         else:
#             isFive = False
#     if 'c' in charMap:
#         cChar = charMap['c']
#         if cChar in digit:
#             isFive = False
#         else:
#             isThree = False
#             isTwo = False
#     if 'e' in charMap:
#         eChar = charMap['e']
#         if eChar in digit:
#             isThree = False
#             isFive = False
#         else:
#             isTwo = False
#     if 'f' in charMap:
#         fChar = charMap['f']
#         if fChar in digit:
#             isTwo = False
#         else:
#             isThree = False
#             isFive = False

#     # Its a 2
#     if isTwo and not isThree and not isFive:
#         charMap['a'] = digit[0]
#         charMap['c'] = digit[1]
#         charMap['d'] = digit[2]
#         charMap['e'] = digit[3]
#         charMap['g'] = digit[4]
#         return True
#     # Its a 3
#     elif isThree and not isTwo and not isFive:
#         charMap['a'] = digit[0]
#         charMap['c'] = digit[1]
#         charMap['d'] = digit[2]
#         charMap['f'] = digit[3]
#         charMap['g'] = digit[4]
#         return True

#     elif isFive and not isTwo and not isThree:
#         charMap['a'] = digit[0]
#         charMap['b'] = digit[1]
#         charMap['d'] = digit[2]
#         charMap['f'] = digit[3]
#         charMap['g'] = digit[4]
#         return True

#     return False


# def decode6(charMap, digit):
#     isSix = True
#     isNine = True
#     isTen = True

#     if 'd' in charMap:
#         dChar = charMap['d']
#         if dChar in digit:
#             isTen = False
#         else:
#             isSix = False
#             isNine = False
#     if 'c' in charMap:
#         cChar = charMap['c']
#         if cChar in digit:
#             isSix = False
#         else:
#             isNine = False
#             isTen = False
#     if 'e' in charMap:
#         eChar = charMap['e']
#         if eChar in digit:
#             isNine = False
#         else:
#             isTen = False
#             isSix = False

#     # Its a 2
#     if isSix and not isTen and not isNine:
#         charMap['a'] = digit[0]
#         charMap['b'] = digit[1]
#         charMap['d'] = digit[2]
#         charMap['e'] = digit[3]
#         charMap['f'] = digit[4]
#         charMap['g'] = digit[5]
#         return True
#     # Its a 3
#     elif isNine and not isSix and not isTen:
#         charMap['a'] = digit[0]
#         charMap['b'] = digit[1]
#         charMap['c'] = digit[2]
#         charMap['d'] = digit[3]
#         charMap['f'] = digit[4]
#         charMap['g'] = digit[5]
#         return True

#     elif isTen and not isNine and not isSix:
#         charMap['a'] = digit[0]
#         charMap['b'] = digit[1]
#         charMap['c'] = digit[2]
#         charMap['e'] = digit[3]
#         charMap['f'] = digit[4]
#         charMap['g'] = digit[5]
#         return True
#     return False


# def decode(digits):
#     charMap = {}

#     while len(digits) > 0:
#         stillMissing = []
#         for digit in digits:
#             if len(digit) == 2:
#                 charMap['c'] = digit[0]
#                 charMap['f'] = digit[1]
#             elif len(digit) == 3:
#                 charMap['a'] = digit[0]
#                 charMap['c'] = digit[1]
#                 charMap['f'] = digit[2]
#             elif len(digit) == 4:
#                 charMap['b'] = digit[0]
#                 charMap['c'] = digit[1]
#                 charMap['d'] = digit[2]
#                 charMap['f'] = digit[3]
#             elif len(digit) == 5:
#                 # 3 2 or a 5
#                 result = decode5(charMap, digit)
#                 if not result:
#                     stillMissing.append(digit)
#             elif len(digit) == 6:
#                 # 0 6 or 9
#                 result = decode6(charMap, digit)
#                 if not result:
#                     stillMissing.append(digit)
#             else:
#                 charMap['a'] = digit[0]
#                 charMap['b'] = digit[1]
#                 charMap['c'] = digit[2]
#                 charMap['d'] = digit[3]
#                 charMap['e'] = digit[4]
#                 charMap['f'] = digit[5]
#                 charMap['g'] = digit[6]

#         digits = stillMissing

#     return charMap


def getNumber(digitMap, digits):
    number = 0
    for digit in digits:
        digit = "".join(sorted(digit))
        num = digitMap[digit]

        number = number * 10
        number += num

    return number


def contains(num, sub):
    for c in sub:
        if c not in num:
            return False
    return True


def diff(left, right):
    d = []
    for c in left:
        if c not in right:
            d.append(c)

    return ''.join(d)


def decode(digits):
    digits = sorted(digits, key=lambda x: len(x))
    for i in range(len(digits)):
        digits[i] = "".join(sorted(digits[i]))
    # We know the map for 1, 2, 4, 8
    digitMap = {
        digits[0]: 1,
        digits[1]: 7,
        digits[2]: 4,
        digits[-1]: 8,
    }
    digits5 = digits[3:6]
    digits6 = digits[6:9]

    three = None
    remainingDigits = []
    # 3 (5 digit) includes 1
    for digit in digits5:
        if contains(digit, digits[0]):
            three = digit
            digitMap[three] = 3

        else:
            remainingDigits.append(digit)

    threeDiffOne = diff(three, digits[0])

    nine = None
    # all 6 digit characters
    for digit in digits6:
        # 9 (6 digit) includes all 4 charactess
        if contains(digit, digits[2]):
            digitMap[digit] = 9
            nine = digit
        # 6 (6 digit) includes all of the 3 - 1 characters
        elif contains(digit, threeDiffOne):
            digitMap[digit] = 6
        # 0 (6 digit) is other
        else:
            digitMap[digit] = 0

    for digit in remainingDigits:
        # 5 (5 digit) is in the 9 digit character
        if contains(nine, digit):
            digitMap[digit] = 5
        else:
            digitMap[digit] = 2

    return digitMap


def part2(filename):
    left, right = parseInput(filename)
    # left = [['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab',
    #         'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']]
    # right = [['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']]
    total = 0

    for i in range(len(left)):
        digitMap = decode(left[i])
        num = getNumber(digitMap, right[i])
        print(num)
        total += num

    return total


if __name__ == '__main__':
    isPart1 = False
    if isPart1:
        total = countUnique(filename)

        print('The answer is:', total)

    else:
        total = part2(filename)

        print('The answer is:', total)
