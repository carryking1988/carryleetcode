# Given an integer n, return the number of prime numbers that are strictly less than n.


# 埃拉托斯特尼筛法(Sieve of Eratosthenes，简称埃氏筛法)是非常常用的，判断一个整数是 否是质数的方法。并且它可以在判断一个整数 n 时，同时判断所小于 n 的整数，因此非常适合这 道题。其原理也十分易懂:从 1 到 n 遍历，假设当前遍历到 m，则把所有小于 n 的、且是 m 的倍 数的整数标为和数;遍历完成后，没有被标为和数的数字即为质数。
import math


# def countPrimes(n):
#     if n <= 2:
#         return 0
#     count = n - 2
#     dic = {}
#     for i in range(1, n + 1):
#         dic[i] = 1
#
#     for i in range(2, n):
#         if dic[i] and isPrime(i):
#             j = 2 * i
#             while j < n:
#                 if dic[j]:
#                     dic[j] = 0
#                     count -= 1
#                 j += i
#     return count
#
#
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True


def countPrimes(n):
    if n < 2:
        return 0
    prime = [True] * n
    prime[0] = prime[1] = False
    # for i in range(2, n):
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i + i, n, i):
                prime[j] = False
    return prime.count(True)


print(countPrimes(10))
print(countPrimes(0))
print(countPrimes(1))
print(countPrimes(1500000))
