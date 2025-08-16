class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        result = ''
        flag = 0
        while current:
            result += str(current.value) + ' ->'
            if current.next == self.head.next and flag == 1:
                break
            flag = 1
            current = current.next
        return result

    def getLength(self):
        length = 0
        current = self.head
        if self.head == self.tail:
            length += 1
        else:
            while current:
                length += 1
                if current.next == self.head:
                    break
                current = current.next
        return length

    def append(self, value):
        current = self.head
        node = Node(value)
        if current is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            current = self.tail
            current.next = node
            node.next = self.head
            self.tail = node

    def prepend(self, value):
        current = self.head
        node = Node(value)
        if current is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node.next = current
            self.tail.next = node
            self.head = node

    def insert(self, index, value) -> bool:
        isInserted = False
        if index == 0:
            self.prepend(value)
            isInserted = True
        elif index == self.getLength() - 1:
            self.append(value)
            isInserted = True
        elif index >= self.getLength():
            isInserted = False
        elif index < self.getLength() - 1:
            node = Node(value)
            current = self.head
            loc = 0
            while loc < index - 1:
                current = current.next
                loc += 1
            node.next = current.next
            current.next = node
            isInserted = True
        return isInserted

    def isEmpty(self):
        return self.head is None


if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    print("--------Checking if Linked List is Empty----------")
    print(csll.isEmpty())
    print("--------Appending data into Linked List----------")
    csll.append(10)
    csll.append(20)
    print(csll)
    print(csll.head.value, csll.tail.value)
    print(csll.isEmpty())
    print("--------Prepending data into Linked List----------")
    csll.prepend(5)
    csll.prepend(-10)
    print(csll)
    print("--------Length of Linked List----------")
    print(csll.getLength())
    print("--------Inserting data into Linked List----------")
    print(csll.insert(2, 100))
    print(csll.insert(4, 50))
    print(csll)
