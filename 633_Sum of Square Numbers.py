# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


def judgeSquareSum(c):
    import math
    left = 0
    right = int(math.sqrt(c))
    while left <= right:
        if left ** 2 + right ** 2 == c:
            return True
        elif left ** 2 + right ** 2 < c:
            left += 1
        else:
            right += 1
    return False
