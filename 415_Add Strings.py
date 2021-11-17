# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
#
# def addStrings(num1, num2):
#     res = ""
#     p = len(num1) - 1
#     q = len(num2) - 1
#     flag = 0
#     while p >= 0 or q >= 0:
#         ele1 = int(num1[p]) if p >= 0 else 0
#         ele2 = int(num2[q]) if q >= 0 else 0
#         temp = ele1 + ele2 + flag
#         flag = 1 if temp >= 10 else 0
#         res = str(temp % 10) + res
#         p -= 1
#         q -= 1
#     return res
def addStrings(num1, num2):
    res = ""
    l1 = list(num1)
    l2 = list(num2)
    flag = 0
    while l1 or l2 or flag:
        ele1 = int(l1.pop()) if l1 else 0
        ele2 = int(l2.pop()) if l2 else 0
        temp = ele1 + ele2 + flag
        flag = 1 if temp >= 10 else 0
        res = str(temp % 10) + res
    return res




num1 = '1'
num2 = '9'
print(addStrings(num1,num2))
