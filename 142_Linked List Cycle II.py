# 对所有节点进行遍历，
# def detectCycle(head):
#     cur = head
#     s = set()
#     while cur:
#         if cur in s:
#             return cur
#         s.add(cur)
#         cur= cur.next
#     return None


def detectCycle(head):
    # 设定快慢指针
    if head and head.next:
        fast = head.next.next
        slow = head.next
    else:
        return None  # 没有闭环
    # 进行循环，首先让快慢指针第一次相遇：
    while fast:
        if fast != slow:
            # 快指针走2步
            if fast.next:
                fast = fast.next.next
            else:
                return None
            # 慢指针走1步
            slow = slow.next
        else:
            detection = head
            while detection != slow:
                detection = detection.next
                slow = slow.next
            return detection