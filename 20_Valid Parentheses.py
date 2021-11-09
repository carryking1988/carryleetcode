#
#
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


def isValid(s):
    """
    :param str: str
    :return: bool
    """
    characters = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in s:
        if char in characters:
            stack.append(char)
        else:
            if not stack or characters[stack.pop()] != char:
                return False
    return not stack



s1 = "()[]{}"
s2 = "([)]"
s3 = "))"
print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
