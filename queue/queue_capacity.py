class Queue:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def __str__(self):
        qlist: list[str] = [str(item) for item in self.items]
        return ' '.join(qlist)

    def enqueue(self, value) -> bool:
        is_added: bool = False
        if not self.is_full():
            self.items.append(value)
            is_added = True
        return is_added

    def dequeue(self) -> bool:
        is_removed = False
        if not self.is_empty():
            self.items.pop(0)
            is_removed = True
        return is_removed

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.max_size


if __name__ == "__main__":
    q = Queue()
    print(f"Is the queue full? {q.is_full()}")
    print(f"Is the queue empty? {q.is_empty()}")
    print("------Inserting data into queue---------")
    q.enqueue(50)
    q.enqueue(100)
    q.enqueue(200)
    print(q)
    print(f"Is inserted? {q.enqueue(400)}")
    print(f"Is inserted? {q.enqueue(600)}")
    print(f"Is inserted? {q.enqueue(700)}")
    print(f"Is the queue full? {q.is_full()}")
    print(q)
    print("------Deleting data from queue---------")
    q.dequeue()
    q.dequeue()
    print(q)
