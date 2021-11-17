# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
#
# Implement the Solution class:
#
# Solution(ListNode head) Initializes the object with the integer array nums.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        res = None
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            temp = random.random()
            if temp <= 1/count:
                res = cur.val
            cur = cur.next
        return res


# Your Solution objebct will be instantiated and called as such:
head = [1, 2, 3]
obj = Solution(head)
param_1 = obj.getRandom()
