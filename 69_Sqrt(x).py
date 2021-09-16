# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#
def mySqrt(x):
    left = 1
    right = x
    while left <= right:
        mid = (left + right) // 2
        result = mid ** 2
        if result == x:
            return mid
        elif result >= x:
            right = mid-1
        else:
            left = mid + 1
    return right


print(mySqrt(100))

# print(mySqrt(8))
