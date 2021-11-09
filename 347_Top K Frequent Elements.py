# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    from collections import Counter
    count = dict(Counter(nums))
    arr = sorted(count.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(k):
        res.insert(0, arr[i][0])
    return res

    # print(count)
    # res = [key for key in count.keys()][:k]
    # return res


nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, ]
k = 2

print(topKFrequent(nums, k))
