# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
#
# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
import bisect
import random


class Solution:
    """
    通过累加计算，将各个index的权重值用sum标示出来，随机产生的数字n通过二分法确定在累加权重数列的位置，由此得到平均概率的权重index
    """
    def __init__(self, w):
        self.arr = [0]
        self.sum = 0
        for i in w:
            self.sum += i
            self.arr.append(self.sum)
        self.sum -= 1

    def pickIndex(self):
        n = random.randint(0, self.sum)
        return bisect.bisect(self.arr, n) - 1


# w = [1, 3]
w = [1, 8, 9, 3, 6]
obj = Solution(w)
param_1 = obj.pickIndex()
