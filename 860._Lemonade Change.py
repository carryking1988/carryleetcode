def lemonadeChange(bills):
    cnt5 = cnt10 = 0
    if bills[0] == 5:
        cnt5 += 1
    else:
        return False

    for i in range(1, len(bills)):
        if bills[i] == 5:
            cnt5 += 1
        elif bills[i] == 10:
            if cnt5 > 0:
                cnt5 -= 1
                cnt10 += 1
            else:
                return False
        elif bills[i] == 20:
            if cnt10 > 0 and cnt5 > 0:
                cnt10 -= 1
                cnt5 -= 1
            elif cnt5 >= 3:
                cnt5 -= 3
            else:
                return False
    return True


bills_1 = [5, 5, 10, 10, 20]
bills_2 = [5, 5, 5, 10, 20]
print(lemonadeChange(bills_1))
print(lemonadeChange(bills_2))
