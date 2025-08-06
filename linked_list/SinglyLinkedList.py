class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        curr = self.head
        while curr is not None:
            result += str(curr.data)
            if curr.next is not None:
                result += '->'
            curr = curr.next
        return result

    def append(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        if self.length > 0:
            temp = self.tail
            self.tail = newNode
            temp.next = self.tail

        self.length += 1

    def prepend(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
        self.length += 1

    def insert(self, data, index):
        if index < 0 or index > self.length + 1:
            return
        if index == 0:
            return self.prepend(data)
        elif index == self.length + 1:
            return self.append(data)
        else:
            newNode = Node(data)
            curr = self.head

            for _ in range(index - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def delete(self, index):
        deletedNode = None
        # if index >= self.length or index < 0:
        #     return
        if self.length == 1 and index == 0:
            temp = self.head
            self.head = None
            self.tail = None
            deletedNode = temp.data
        elif self.length > 1 and index == 0:
            temp = self.head
            self.head = self.head.next
            deletedNode = temp.data
        elif self.length > 1 and index == self.length - 1:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            temp = self.tail
            self.tail = curr
            self.tail.next = None
            deletedNode = temp.data
        elif self.length > 1 and index < self.length - 1:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            deletedNode = temp.data

        if deletedNode is not None:
            self.length -= 1
        return deletedNode

    def getLength(self):
        return self.length


if __name__ == "__main__":
    sll = SinglyLinkedList()
    print("-------Inserting data into Linked List--------")
    sll.append(10)
    sll.append(20)
    sll.append(30)

    sll.prepend(5)
    sll.prepend(-2)

    sll.insert(25, 2)
    sll.insert(40, 7)

    print(sll)
    print("-------Traversing through the Linked List--------")
    sll.traverse()
    print("-------Deleting elements from the Linked List--------")
    print(sll)
    print(f"Deleting first element: {sll.delete(0)}")
    print(sll)
    print(f"Deleting last element: {sll.delete(5)}")
    print(sll)
    print(f"Deleting third element: {sll.delete(2)}")
    print(sll)

