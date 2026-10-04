class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        cur = self.head.next

        for i in range(index):
            if cur is self.tail:
                return -1
            else:
                cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        
        cur = self.head.next

        for _ in range(index):
            if cur is self.tail:
                return
            else:
                cur = cur.next
        
        node = ListNode(val)

        node.prev = cur.prev
        node.next = cur
        cur.prev.next = node
        cur.prev = node
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        
        cur = self.head.next

        for _ in range(index):
            if cur is self.tail:
                return
            else:
                cur = cur.next
        
        if cur is self.tail:
            return

        cur.prev.next = cur.prev.next.next
        cur.next.prev = cur.next.prev.prev
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)