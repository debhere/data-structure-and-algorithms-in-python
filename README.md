# Data Structures & Algorithms in Python
This repo contains the implementation and demonstration of different data structures &amp; algorithm implementation in Python.

## Linked List
A Linked List is a data structure consisting of a sequence of nodes, where each node contains data and a pointer to the next node in the sequence.

### Core Principle
It eschews contiguous memory allocation, instead chaining nodes together via references. This design makes memory utilization dynamic and flexible.

### Key Variants & Their Nature
Singly Linked List (Linear): The base form. Has a head (start) and a tail (end) that points to null. This is a linear, acyclic structure.
Doubly Linked List (Linear): Nodes have pointers to both the next and previous nodes, enabling bidirectional traversal. Remains linear if null-terminated.
Circular Linked List (Non-Linear): The tail's pointer connects back to the head, forming a cycle. This circular reference makes it a non-linear, cyclic structure.

### The Trade-Off
This pointer-based architecture provides **O(1)** time complexity for insertions/deletions at known positions but sacrifices **O(n)** time complexity for random access, as traversal from the head is always required.
In essence, it's the foundational structure for prioritizing efficient mutations over fast lookup.

## Stack
A Stack is a linear, abstract data type (ADT) that follows the Last-In, First-Out (LIFO) principle. The last element added is the first element to be removed.

### Core Mechanics 
Interaction is restricted to one end, typically called the top. The two fundamental operations are:
**_Push:_** Adds an element to the top of the stack.
**_Pop:_** Removes and returns the top element.

### Underlying Implementation 
A stack is defined by its behavior, not its implementation. It can be implemented using various underlying data structures, most commonly:
A Linked List (using the head as the top).
A List (in Python).

### Key Characteristics
All core operations (Push, Pop, Peek) are **O(1)** constant time when implemented correctly.

### Use Cases 
It is the fundamental structure for managing function call execution, recursion, undo/redo features, and depth-first search algorithms.

In essence, a stack is a minimalist, high-performance data structure for managing elements in a strict reverse order of arrival.