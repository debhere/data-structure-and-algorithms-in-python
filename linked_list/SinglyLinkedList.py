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
        if index < 0 or index == self.length + 2:
            return
        if index == 0:
            self.prepend(data)
        elif index == self.length + 1:
            self.append(data)
        else:
            newNode = Node(data)
            curr = self.head

            for _ in range(index - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.length += 1

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

    print(sll)
