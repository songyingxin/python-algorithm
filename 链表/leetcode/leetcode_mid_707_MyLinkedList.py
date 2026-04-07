
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1
        
        node = self.head
        for i in range(index+1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        
        index = max(0, index)
        self.size += 1
        new_node = ListNode(val)

        node = self.head
        for i in range(index):
            node = node.next
        
        new_node.next = node.next
        node.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1

        node = self.head
        for _ in range(index):
            node = node.next
        
        node.next = node.next.next
