class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        result = ''
        curr = self.head
        while curr:
            result += str(curr.value)
            if curr.next is not None:
                result += '<->'
            curr = curr.next
        return result

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def appendNode(self, value) -> bool:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            isAppended = True
        else:
            temp = self.tail
            temp.next = node
            node.prev = temp
            self.tail = node
            isAppended = True
        return isAppended

    def prependNode(self, value) -> bool:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            isPrepended = True
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node
            isPrepended = True
        return isPrepended

    def insertNode(self, index: int, value) -> bool:
        if index == 0:
            return self.prependNode(value)
        curr = self.head
        loc: int = 0
        isInserted = False
        while curr:
            if loc == index:
                node = Node(value)
                node.prev = curr.prev
                curr.prev.next = node
                node.next = curr
                curr.prev = node
                isInserted = True
                break
            curr = curr.next
            loc += 1
        return isInserted

    def reverseTraversal(self):
        curr = self.tail
        while curr:
            print(curr.value)
            curr = curr.prev

    def find(self, target) -> int:
        curr = self.head
        idx = 0
        isFound = False
        while curr:
            if curr.value == target:
                isFound = True
                break
            curr = curr.next
            idx += 1
        return idx if isFound else -1

    def getValue(self, index: int):
        nodeVal = None
        idx = 0
        curr = self.head
        while curr:
            if idx == index:
                nodeVal = curr.value
                break
            curr = curr.next
            idx += 1
        return nodeVal

    def setValue(self, index, target):
        curr = self.head
        isSet = False
        idx = 0
        while curr:
            if idx == index:
                curr.value = target
                isSet = True
                break
            curr = curr.next
            idx += 1
        return isSet

    def remove(self, index: int):
        deletedNode = None
        curr = self.head
        idx = 0
        while curr:
            if self.head == self.tail and index == idx:
                deletedNode = self.head.value
                self.head = None
                self.tail = None
                break
            elif curr == self.tail and index == idx:
                temp = self.tail
                curr.prev.next = None
                self.tail = curr.prev
                temp.prev = None
                deletedNode = temp.value
                break
            elif curr == self.head and index == idx:
                temp = curr
                self.head = curr.next
                self.head.prev = None
                curr.next.prev = self.head
                temp.next = None
                deletedNode = temp.value
                break
            elif idx == index:
                temp = curr
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                temp.prev = None
                temp.next = None
                deletedNode = temp.value
                break
            curr = curr.next
            idx += 1

        return deletedNode

    def removeAll(self):
        self.head = None
        self.tail = None


dll = DoublyLinkedList()
print("-------Appending into Doubly Linked List--------")
dll.appendNode(10)
dll.appendNode(20)
print(dll)
print("-------Prepending into Doubly Linked List--------")
dll.prependNode(5)
print(dll)
print("-------Iterating through the Doubly Linked List--------")
for val in dll:
    print(val.value, end=' ')

print("\n-------Inserting into Doubly Linked List--------")
dll.insertNode(0, 1)
dll.insertNode(1, 7)
dll.insertNode(3, 18)
dll.insertNode(12, 40)
print(dll)
print("-------Finding element in Doubly Linked List--------")
print(dll.find(7))
print(dll.find(20))
print(dll.find(100))
print("-------Getting element in Doubly Linked List based on index--------")
print(dll.getValue(3))
print(dll.getValue(2))
print(dll.getValue(10))
print("-------Setting element in Doubly Linked List based on index--------")
print(dll)
print(dll.setValue(2, 15), dll.setValue(5, 50))
print(dll)
print("-------Deleting element in Doubly Linked List based on index--------")
# print(dll.remove(0), dll.remove(1), dll.remove(4), dll.remove(10))
dll.remove(0)
dll.remove(2)
dll.remove(3)
print(dll)
print("-------Traverse elements in Reverse--------")
dll.appendNode(30)
dll.prependNode(5)
dll.reverseTraversal()
print("-------Deleting elements in Reverse--------")
dll.removeAll()
print(dll)