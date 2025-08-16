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

    def isEmpty(self):
        return self.head is None


if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    print("--------Checking if Linked List is Empty----------")
    print(csll.isEmpty())
    print("--------Appending data in Linked List----------")
    csll.append(10)
    csll.append(20)
    print(csll)
    print(csll.head.value, csll.tail.value)
    print(csll.isEmpty())
