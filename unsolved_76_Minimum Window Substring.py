#  Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.

def minWindow(s, t):
    """s, t all str"""
    from collections import defaultdict
    mem = defaultdict(int)
    for char in t:
        mem[char] += 1
    t_len = len(t)
    minleft, minright = 0, len(s)
    left = 0
    for right, char in enumerate(s):
        if mem[char] > 0:
            t_len -= 1
        mem[char] -= 1

        if t_len == 0:
            while mem[s[left]] < 0:
                mem[s[left]] += 1
                left += 1

            if right - left < minright - minleft:
                minleft, minright = left, right

            mem[s[left]] += 1
            t_len += 1
            left += 1
    return "" if minright == len(s) else s[minleft:minright + 1]


s = 'helloworld'
t = 'oe'
print(minWindow(s, t))
