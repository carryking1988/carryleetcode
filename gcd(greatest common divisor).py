# 求得两个数的最大公因数(greatest common divisor, gcd)


def gcd(a, b):
    return gcd(b, a % b) if a % b != 0 else b


a = 32
b = 6
print(gcd(a, b))


# 求两个数的最小公倍数(least common multiple,lcm)
def lcm(a, b):
    return int(a * b / gcd(a, b))


print(lcm(a, b))


# 扩展欧几里得算法(extended gcd),在求得 a 和 b 最大公因数的同 时，也得到它们的系数 x 和 y，从而使 ax + by = gcd(a, b)。


