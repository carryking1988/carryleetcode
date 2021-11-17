# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


def hammingWeight(n):
    n = int()
    count = 0
    while n > 0:
        count += (n & 1)
        n >>= 1
    return count

n = 11111111111111111111111111111101
print(hammingWeight(n))