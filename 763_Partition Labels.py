# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
#
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "s "
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

from collections import OrderedDict


# def partitionLabels(s):
#     char_dict = {}
#     for index, char in enumerate(s):
#         if char not in char_dict.keys():
#             char_dict[char] = [0, 0]
#             char_dict[char][0] = index
#         else:
#             char_dict[char][1] = index
#
#     result = []
#
#     temp = s[0]
#     start, end = char_dict[temp][0], char_dict[temp][1]
#     while True:
#         if end > start:
#             for char in s[start:end]:
#                 if char_dict[char][1] > end:
#                     end = char_dict[char][1]
#             result.append(end - start + 1)
#         else:
#             result.append(1)
#         if end + 1 < len(s):
#             temp = s[end + 1]
#             start, end = char_dict[temp][0], char_dict[temp][1]
#         else:
#             break
#     return result

def partitionLabels(s):
    lindex = {c: i for i, c in enumerate(s)}
    print(lindex)
    left = right = 0
    result = []
    for idx, char in enumerate(s):
        right = max(right, lindex[char])
        if idx == right:
            result.append(right - left + 1)
            left = right + 1
    return result


# s = "eccbbbbdec"
# s = "ababcbacadefegdehijhklij"
s = "caedbdeddafiighfq"
print(partitionLabels(s))
