class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class LinkedList:
    def __init__(self):
        self.top = None


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        stk = []
        curr = self.linked_list.top
        while curr is not None:
            stk.insert(0, str(curr.value))
            curr = curr.prev
        return ' '.join(stk)

    def push(self, value):
        node = Node(value)
        if self.linked_list.top is None:
            self.linked_list.top = node
        else:
            temp = self.linked_list.top
            node.prev = temp
            self.linked_list.top = node

    def peek(self):
        return self.linked_list.top.value

    def is_empty(self):
        return self.linked_list.top is None

    def pop(self):
        curr = self.linked_list.top
        self.linked_list.top = self.linked_list.top.prev
        curr.prev = None

    def clear(self):
        self.linked_list.top = None


if __name__ == "__main__":
    stack = Stack()

    print("----------Inserting elements into Stack-------------")
    print(f"Check if the stack is empty: {stack.is_empty()}")
    stack.push(200)
    stack.push(30)
    stack.push(10)
    print(f"Check if the stack is empty: {stack.is_empty()}")
    print(stack)
    print(f"Check the top element: {stack.peek()}")
    print("----------Deleting elements from Stack-------------")
    stack.pop()
    print(stack)
    print("----------Clearing the Stack-------------")
    print(f"Check if the stack is empty: {stack.is_empty()}")
    stack.clear()
    print(f"Check if the stack is empty: {stack.is_empty()}")

