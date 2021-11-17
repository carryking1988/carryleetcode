class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, val):
        if index <= 0:
            self.add(val)
        elif index >= self.length():
            self.append(val)
        else:
            node = Node(val)
            cur = self.head
            for i in range(index):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, val):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self, val):
        return val in self.items()
