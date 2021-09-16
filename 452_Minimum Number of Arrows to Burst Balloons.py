# There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.
#

def findMinArrowShots(points):
    points.sort(key=lambda x: (x[1], x[0]))
    print(points)
    temp = points[0][1]
    amount = 1
    for i in range(1, len(points)):
        if temp < points[i][0]:
            amount += 1
            temp = points[i][1]
    return amount

# 双指针法
# def findMinArrowShots(points):
#     if not points or len(points) == 0:
#         return 0
#     points.sort(key=lambda x: x[0])
#     result = []
#     start, end = points[0][0], points[0][1]
#     for i in range(1, len(points)):
#         s, e = points[i][0], points[i][1]
#         if s <= end:
#             start, end = s, min(end, e)
#         else:
#             result.append([start, end])
#             start, end = s, e
#     result.append([start, end])
#     return len(result)


# points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# points = [[1, 2], [3, 4], [5, 6], [7, 8]]
# points = [[1, 2], [2, 3], [3, 4], [4, 5]]
points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
# points.sort(key=lambda x: x[0])
# print(points)
print(findMinArrowShots(points))

# Example 1:
# Input: points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# Output: 2

# Example 2:
# Input: points = [[1, 2], [3, 4], [5, 6], [7, 8]]
# Output: 4

# Example 3:
# Input: points = [[1, 2], [2, 3], [3, 4], [4, 5]]
# Output: 2
#
# Constraints:
#
# 1 <= points.length <= 104
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1
