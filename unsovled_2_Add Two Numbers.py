# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

l1 = [2, 4, 3]
l2 = [5, 6, 4]


# def assembleList(l1):
#     sum = 0
#     n = len(l1)-1
#     while l1:
#         sum += l1.pop() * 10 ** n
#         n -= 1
#     return sum
#
# print(assembleList(l1))
# print(assembleList(l2))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        while l1 or l2:
            pass


n1 = ListNode()
p = n1
print(id(n1))
print(id(p))
