# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
#
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


def reverse(x):
    if x > 0:
        a = str(x)
        a = a[::-1]
        return int(a) if int(a) <= 2 ** 31 - 1 else 0
    else:
        x = -1 * x
        a = str(x)
        a = a[::-1]
        return -1 * int(a) if int(a) <= 2 ** 31 - 1 else 0


x = 301

print(reverse(x))
