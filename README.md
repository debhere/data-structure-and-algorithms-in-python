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
This pointer-based architecture provides O(1) time complexity for insertions/deletions at known positions but sacrifices O(n) time complexity for random access, as traversal from the head is always required.
In essence, it's the foundational structure for prioritizing efficient mutations over fast lookup.