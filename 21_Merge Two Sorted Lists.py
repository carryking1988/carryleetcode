class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    head = ListNode()
    first = head
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    if l1 == None:
        head.next = l2
    if l2 == None:
        head.next = l1
    return first.next

