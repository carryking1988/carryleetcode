# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


def titleToNumber(columnTitile):
    s = columnTitile[::-1]
    i = 0
    sum = 0
    for char in s:
        sum += 26 ** i * (ord(char) - 64)
        i += 1
    return sum

columnTitle1 = "ZY"
columnTitle2 = 'AB'
print(titleToNumber(columnTitle1))
print(titleToNumber(columnTitle2))