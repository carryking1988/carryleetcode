#
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

def getIntersectionNode(headA,headB):
    if headA is None or headB is None:
        return None
    pa = headA
    pb = headB
    while pa != pb:
        # if pa is None:
        #     pa = headB
        # else:
        #     pa = pa.next
        pa = headB if pa is None else pa = pa.next
        pb = headA if pb is None else pb = pb.next
    return pa

