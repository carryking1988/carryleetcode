# Given the head of a singly linked list, return true if it is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head):
    rev = None
    original_list = head
    while original_list:
        rev = ListNode(original_list.val,rev)
        original_list = original_list.next
    return True if rev == head else False
