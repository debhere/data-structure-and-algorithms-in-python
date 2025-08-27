from typing import Any


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

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value)
            if curr == self.tail:
                break
            curr = curr.next

    def getLength(self):
        length = 0
        current = self.head
        if self.head is not None and self.head == self.tail:
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

    def remove(self, data) -> bool:
        temp = self.head
        is_found = False
        if self.head.value == data:
            self.head = self.head.next
            self.tail.next = self.head
            is_found = True
        else:
            while temp:
                if temp.next.value == data:
                    if temp.next == self.tail:
                        self.tail = temp
                        self.tail.next = self.head
                    else:
                        temp.next = temp.next.next
                    is_found = True
                    break
                if temp == self.tail:
                    break
                temp = temp.next
        return is_found

    def remove_all(self):
        self.head = None
        self.tail = None


if __name__ == "__main__":
    circularSingly = CircularSinglyLinkedList()
    print("--------Checking if Linked List is Empty----------")
    print(circularSingly.isEmpty())
    print("--------Appending data into Linked List----------")
    circularSingly.append(10)
    circularSingly.append(20)
    print(circularSingly)
    print(circularSingly.head.value, circularSingly.tail.value)
    print(circularSingly.isEmpty())
    print("--------Prepending data into Linked List----------")
    circularSingly.prepend(5)
    circularSingly.prepend(-10)
    print(circularSingly)
    print("--------Length of Linked List----------")
    print(circularSingly.getLength())
    print("--------Inserting data into Linked List----------")
    print(circularSingly.insert(2, 100))
    print(circularSingly.insert(4, 50))
    print(circularSingly)
    print(f"Check if the list is empty: {circularSingly.isEmpty()}")
    print("--------Deleting data from Linked List----------")
    print(circularSingly.remove(100))
    print(circularSingly)
    print(circularSingly.head.value, circularSingly.tail.value)
    print(circularSingly.remove(50))
    print(circularSingly)
    print(circularSingly.head.value, circularSingly.tail.value)
    print(circularSingly.remove(-10))
    print(circularSingly)
    print(circularSingly.remove(200))
    print(circularSingly)
    print(circularSingly.getLength())
    print("--------Traversing through the Linked List----------")
    circularSingly.traverse()
    print("--------Deleting all elements----------")
    print(f"Length of thee list: {circularSingly.getLength()}")
    circularSingly.remove_all()
    print(f"Length of the list after removing all elements: {circularSingly.getLength()}")


