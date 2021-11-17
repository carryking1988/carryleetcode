# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution(object):
    def isPowerOfFour(self, n):
        # return n == 1 or n != 0 and n % 4 == 0 and self.isPowerOfFour(n // 4)

        from math import ceil, log, floor
        return ceil(log(n, 4)) == floor(log(n, 4)) if n > 0 else False


n1 = 10
n2 = 16
n3 = 24
s = Solution()
print(s.isPowerOfFour(n1))
print(s.isPowerOfFour(n2))
print(s.isPowerOfFour(n3))
