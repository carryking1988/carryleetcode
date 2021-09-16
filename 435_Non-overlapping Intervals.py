def func(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    # print(intervals)
    total = 0
    prev = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev:
            total += 1
        else:
            prev = intervals[i][1]
    return total


intervals = [[1,2],[2,3],[3,4],[1,3]]
# intervals = [[1, 2], [1, 2], [1, 2]]

print(func(intervals))
