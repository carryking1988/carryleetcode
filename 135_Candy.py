def getcandy(ratings):
    candy_list = [1 for _ in range(len(ratings))]
    i = 0
    while i < len(ratings) - 1:
        if ratings[i] < ratings[i + 1]:
            candy_list[i + 1] = candy_list[i] + 1
        i += 1
    j = len(ratings) - 1
    while j > 0:
        if ratings[j] < ratings[j - 1] and candy_list[j - 1] <= candy_list[j]:
            candy_list[j - 1] = candy_list[j] + 1
        j -= 1
    return sum(candy_list)

ratings = [1,0,2]

print(getcandy(ratings))
