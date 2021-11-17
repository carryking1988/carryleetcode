# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

def convertToTitle(num):
    res = ""
    while num != 0:
        res = chr((num - 1) % 26 + 65) + res
        num = (num - 1) // 26
    return res


print(convertToTitle(28))
