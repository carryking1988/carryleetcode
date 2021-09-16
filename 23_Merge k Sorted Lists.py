#  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    result = []
    for linklist in lists:
        while linklist:
            result.append(linklist.val)
            linklist = linklist.next
    if result == []:
        return []

    result.sort()
    newlinklist = ListNode(0)
    first = newlinklist
    while result:
        newlinklist.next = ListNode(result.pop(0))
        newlinklist = newlinklist.next
    return first.next


