class Solution(object):
    def isPowerOfTwo(self, n):
        """
        2的幂，1 2 4 8 16 64
        二进制 1 10 100 1000 10000 100000
        如果是2的幂，那么只能是 1 + 0 0 0 0
        当且只有右移到最后一位为1，count = 1，之前有1全部false
        """
        count = 0
        while n > 0:
            count += (n & 1) # 这里&是二进制的按位运算符，如果两个值都是1，则按位结果为1，否则为0
            n >>= 1 # >> 是右移运算符，把左边的数字的二进制全部右移一位。
        return count == 1


n1 = 10
n2 = 16
n3 = 24
n4 = 11
s = Solution()
print(s.isPowerOfTwo(n1))
print(s.isPowerOfTwo(n2))
print(s.isPowerOfTwo(n3))
print(s.isPowerOfTwo(n4))
