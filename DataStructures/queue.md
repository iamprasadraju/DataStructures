# Queue

A **Queue** is a fundamental linear data structure that organizes elements in a specific order, following the First-In, First-Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed, much like a line of people waiting for service: the person at the front of the line is served firstA queue is a fundamental linear data structure that organizes elements in a specific order, following the First-In, First-Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed, much like a line of people waiting for service: the person at the front of the line is served first


![img](https://miro.medium.com/v2/resize:fit:1001/0*7fDsAPlAoFEca0sW.png)


## How a Queue Works:

- **Enqueue**: Adding an element to the rear (end) of the queue.

- **Dequeue**: Removing an element from the front (beginning) of the queue.

- The front of the queue is where elements are removed, and the rear is where new elements are added


## Key Characteristics:

- **FIFO Structure**: Ensures elements are processed in the order they arrive.

- **Linear Data Structure**: Elements are arranged sequentially.

- **Dynamic Size**: Queues can grow or shrink as elements are added or removed.

- **Limited Access**: Only the front and rear elements can be accessed directly, not the middle elements


## Types of Queues:

| Type                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| Simple (Linear)         | Standard queue; insert at rear, remove from front.                         |
| Circular Queue          | Last element connects to the first, forming a circle for efficient memory use. |
| Priority Queue          | Elements are removed based on priority, not just arrival order.            |
| Double-Ended Queue (Deque) | Insertion and deletion allowed at both ends.                              |


## Queue Interface:

- `enqueue(E item)` → Adds an element to the rear of the Queue. → **O(1)**  
- `dequeue()` → Removes the front element from the Queue. → **O(1)**  
- `peek()` → Returns the front element without removing it. → **O(1)**  
- `isEmpty()` → Checks if the Queue is empty. → **boolean** → **O(1)**  
- `size()` → Returns the number of elements in the Queue. → **int** → **O(1)**  


## Where to Use Queues:

- **Task Scheduling**: Managing tasks in operating systems and job queues.

- **Buffering**: Handling data streams, such as print spooling or network packet management.

- **Breadth-First Search (BFS)**: Used in graph traversal algorithms.

- **Request Handling**: Managing requests in web servers and other services.



### Implementation of Linked Lists:


```python

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to end (O(1) append)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front (O(n) pop(0))"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """View front item without removal"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


```