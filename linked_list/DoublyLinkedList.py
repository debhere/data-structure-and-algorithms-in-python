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
            self.head = node
            isPrepended = True
        return isPrepended

    def insertNode(self, index, value):
        pass


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

