# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            delete_last = s[left: right]
            delete_first = s[left + 1: right + 1]
            return delete_last == delete_last[::-1] or delete_first == delete_first[::-1]
        left += 1
        right -= 1
    return True


s = 'dceabacd'
print(validPalindrome(s))

print(s[::-1])
print(s)


def validPalindrome2(s):
    rever = s[::-1]
    if rever == s:
        return True
    else:
        for idx, char in enumerate(s):
            if rever[idx] != char:
                rever = rever[0:idx] + rever[idx + 1:]
                if rever == rever[::-1]:
                    return True
                s = s[0:idx] + s[idx + 1:]
                return s == s[::-1]


print(validPalindrome2(s))
