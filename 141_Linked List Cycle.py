# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
# def hasCycle(head):
#     s = set()
#     if not head:
#         return False
#     else:
#         while head:
#             if head not in s:
#                 s.add(head)
#                 head = head.next
#             else:
#                 return True
#         return False

def hasCycle(head):
    fast = slow = head
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False













