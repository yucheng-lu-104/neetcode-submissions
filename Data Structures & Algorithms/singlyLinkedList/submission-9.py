class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        curr = self.head

        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        
        return curr.value if curr else -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        
    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
            if prev is None:
                return False
        if prev.next is None:
            return False
        
        if prev.next is self.tail:
            self.tail = prev
        
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.value)
            curr = curr.next
        
        return res
        
