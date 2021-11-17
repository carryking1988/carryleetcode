# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

def checkPowersOfThree(n):
    while n > 0:
        if n % 3 > 1:
            return False
        n //= 3
    return True

print(checkPowersOfThree(12))
print(checkPowersOfThree(21))
print(checkPowersOfThree(91))
print(checkPowersOfThree(100))