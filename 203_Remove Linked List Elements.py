# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# def removeElements(head,val):
#     while head and head.val == val:
#         head = head.next
#     q = head
#     p = q.next
#     while p:
#         if p.val == val:
#             q.next = p.next
#         else:
#             q = q.next
#         p = p.next
#     return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    starter = ListNode()
    starter.next = head

    prev = starter
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return starter.next


# start = ListNode(None)
# start.next = head
#
# prev = start
# cur = head
#
# while cur:
#     if cur.val == val:
#         prev.next = cur.next
#     else:
#         prev = prev.next
#     cur = cur.next
#
# return start.next

