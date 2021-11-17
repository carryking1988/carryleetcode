# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

def trailingZeroes(n):
    res = 0
    i = 5
    while n >= i:
        res += n // i
        i *= 5
    return res


n = 30
print(trailingZeroes(n))
