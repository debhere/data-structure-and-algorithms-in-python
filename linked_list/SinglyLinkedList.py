class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        result = ''
        curr = self.head
        while curr is not None:
            result += str(curr.data)
            if curr.next is not None:
                result += '->'
            curr = curr.next
        return result

    def append(self, data) -> None:
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        if self.length > 0:
            temp = self.tail
            self.tail = newNode
            temp.next = self.tail

        self.length += 1

    def prepend(self, data) -> None:
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
        self.length += 1

    def insert(self, data, index: int) -> None:
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

    def traverse(self) -> None:
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def delete(self, index: int) -> int | None:
        deletedNode = None

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
            for _ in range(index - 1):
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

    def find(self, value) -> int:
        curr = self.head
        searchedIndex = -1
        isFound = False
        while curr:
            searchedIndex += 1
            if curr.data == value:
                isFound = True
                break
            curr = curr.next
        return searchedIndex if isFound else -1

    def update(self, original, target) -> bool:
        isUpdated = False
        curr = self.head

        while curr:
            if curr.data == original:
                curr.data = target
                isUpdated = True
                break
            curr = curr.next

        return isUpdated

    def getValue(self, index) -> int | None:
        element = None
        if index < 0:
            index = self.length - abs(index)
        if self.length - 1 >= index > 0:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            element = curr.data
        return element

    def setValue(self, index, target) -> bool:
        isValueSet = False
        if index < 0:
            index = self.length - abs(index)
        if self.length - 1 >= index > 0:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.data = target
            isValueSet = True
        return isValueSet

    def deleteLinkedList(self):
        self.head = None
        self.tail = None
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
    print("-------Finding element in the Linked List--------")
    print(f"Finding 100: {sll.find(100)}")
    print(f"Finding 20: {sll.find(20)}")
    print("-------Update element in the Linked List--------")
    print(f"Update 20 to 25: {sll.update(20, 27)}")
    print(f"Update 50 to 60: {sll.update(50, 60)}")
    print(sll)
    print("-------Get element in the Linked List based on index--------")
    print(f"Getting value of index 2: {sll.getValue(2)}")
    print(f"Getting value of index -1: {sll.getValue(-1)}")
    print(f"Getting value of index -12: {sll.getValue(-12)}")
    print("-------Set value in the Linked List based on index--------")
    print(sll)
    print(f"Setting value for index 2: {sll.setValue(2, 30)}")
    print(f"Setting value for index 3: {sll.setValue(3, 50)}")
    print(f"Setting value for index 10: {sll.setValue(10, 100)}")  # Invalid inputs
    print(sll)
    print("-------Delete entire linked list--------")
    sll.deleteLinkedList()
    print(f"Linked List is empty: {sll}")
