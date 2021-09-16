# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    rev = None
    while head:
        rev = ListNode(head.val, rev)
        head = head.next
    return rev
