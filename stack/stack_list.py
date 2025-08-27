from typing import Any


class Stack:
    def __init__(self):
        self.elements: list[Any] = []

    def __str__(self):
        ret = ''
        for element in self.elements:
            ret += str(element) + ' '
        return ret

    def push(self, value: Any) -> None:
        self.elements.append(value)

    def peek(self) -> Any:
        return self.elements[-1]

    def pop(self) -> None:
        self.elements.pop(-1)

    def is_empty(self) -> bool:
        res = False
        if len(self.elements) == 0:
            res = True
        return res

    def clear(self) -> None:
        self.elements.clear()


if __name__ == "__main__":
    myStack = Stack()

    print("----------Inserting elements into Stack-------------")
    print(f"Check if the stack is empty: {myStack.is_empty()}")
    myStack.push(10)
    myStack.push(15)
    myStack.push(22)
    print(myStack)
    print(f"Check if the stack is empty: {myStack.is_empty()}")
    print(f"Value at the top of the stack: {myStack.peek()}")
    print("----------Deleting elements into Stack-------------")
    myStack.pop()
    print(myStack)
    print(f"Value at the top of the stack: {myStack.peek()}")
    print("----------Clearing the Stack-------------")
    myStack.clear()
    print(f"Check if the stack is empty: {myStack.is_empty()}")
