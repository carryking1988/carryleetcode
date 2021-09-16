def canPlaceFlowers(flowerbed, n):
    count = 0
    # if len(flowerbed) <=2:
    #     return 1 if sum(flowerbed) == 0 else 0

    # for i in range(len(flowerbed)):
    #     if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] ==0:
    #         total += 1
    # return total

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
    return n <= count
