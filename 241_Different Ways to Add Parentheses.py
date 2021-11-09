# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.


# def diffWaysToCompute(self, expression: str) -> List[int]:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
import itertools


def diffWaysToCompute(expression):
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    pass


# Input:
expression = "2-1-1"
# Output: [0,2]
