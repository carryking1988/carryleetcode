# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


def deleteDuplicates(head):
    if head == None or head.next == None:
        return head
    current = head
    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next
    return head




