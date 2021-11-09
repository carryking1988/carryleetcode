# Given an integer num, return a string of its base 7 representation.
#
def convertToBase7(num):
    if num >= 0:
        flag = True
    else:
        num = -num
        flag = False
    li = [x for x in range(7)]
    ret = []
    while True:
        a = num // 7 # 商
        b = num % 7 # 余
        ret = [b] + ret
        if a == 0:
            break
        num = a
    result = "".join(str(li[i]) for i in ret)
    return result if flag else '-'+result




num = 102
# output: '202'
print(convertToBase7(num))

num2 = -7
# output : -10
print(convertToBase7(num2))