# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):

    a = list(a)
    b = list(b)
    res = ""
    carry = 0
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        res = str(carry % 2) + res
        carry = carry // 2
    return res


# a = "1010"
# b = "1011"
a = "11"
b = "1"
print(addBinary(a, b))
