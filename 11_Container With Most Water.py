#  Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.

def maxArea(lis):
    result = 0
    left = 0
    right = len(lis) - 1
    while left < right:
        result = max(result, min(lis[left], lis[right]) * (right - left))
        if lis[left] < lis[right]:
            left += 1
        else:
            right -= 1
    return result
# lis = [1,3,5]
lis = [1,8,6,2,5,4,8,3,7]


print(maxArea(lis))