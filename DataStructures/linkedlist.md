# Linked List


A **Linked List** is a linear data structure consisting of a sequence of elements called nodes. Each node contains two parts:

- **Data**: The value or information stored in the node.

- **Pointer** (or link): A reference to the next node in the sequence.


The first node is known as the head, and the last node points to NULL, indicating the end of the list

![image](https://media.geeksforgeeks.org/wp-content/uploads/20220829152206/LLdrawio.png)


## Key Characteristics:

- Dynamic Size: Linked lists can grow or shrink in size as needed, making them ideal for situations where the number of elements is unknown in advance.

- Non-contiguous Memory: Unlike arrays, linked list nodes do not need to be stored in consecutive memory locations. Each node can be placed wherever there is free space in memory, and the links maintain the order.

- Efficient Insertions/Deletions: Adding or removing nodes does not require shifting other elements, making these operations efficient compared to arrays.


## Types of Linked Lists:


- **Singly Linked List**: Each node points to the next node only.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png)

- **Doubly Linked List**: Each node has pointers to both the next and the previous node, allowing traversal in both directions.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

- **Circular Linked List**: The last node points back to the first node, forming a circle

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/350px-Circularly-linked-list.svg.png)


## Linked list Interface:

- `build(iter)` --> Creates a Linked list from an iterable -> O(n)

- `get_at(i: index)` --> Returns the element at given index -> O(i) : Traverses

- `set_at(x, i: index)` --> Updates the value at index i with x. -> O(i)

- `insert_first(x)` --> Inserts a new node at the beginning of the list. -> O(1)

- `delete_first()` --> Removes the first node from the list and return node.item -> O(1)

- `insert_at(x, i:index)` --> inserts x at index i -> O(i)

- `delete_at(i: index)` --> Removes the node at index i and return node.item  ->  O(i)

- `insert_last(x)` --> insert x at the end of the linkedlist -> O(n)

- `delete_last()` --> Remove the last node from the linkedlist and return node.item -> O(n)


## Where to Use Linked lists:

Linked lists are ideal in scenarios where efficient insertion, deletion, and dynamic memory management are required. Their flexibility and structure make them suitable for a wide range of applications in both software systems and real-world technologies.


- **Implementing Queues and Stacks**  
  Linked lists are commonly used to implement FIFO (First-In-First-Out) queues and LIFO (Last-In-First-Out) stacks, where frequent insertions and deletions at the ends are required. Linked lists provide constant time (O(1)) operations for these use cases, unlike arrays which may require shifting elements.

- **Music and Media Playlists**  
  In music or video players, linked lists manage playlists, allowing easy insertion, deletion, and rearrangement of songs or videos without shifting large blocks of memory.

- **Web Browsing History**  
  Browsers use linked lists to maintain the history of visited pages. The back and forward navigation buttons traverse this linked structure, enabling seamless movement through browsing history.

- **Undo/Redo Functionality**  
  Text editors and graphic design software use linked lists to store user actions. Each action is a node, allowing the application to traverse backward for undo operations and forward for redo operations.

- **Image Viewers**  
  Linked lists organize images, enabling users to move to the next or previous image efficiently, as each image node points to its neighbors.

- **Dynamic Memory Management**  
  Operating systems use linked lists to manage free memory blocks, supporting dynamic allocation and deallocation of memory.

- **File Systems**  
  Many file systems represent directories and files as linked lists, supporting hierarchical navigation and efficient file management.

- **Graph and Sparse Matrix Implementations**  
  Adjacency lists for graphs and sparse matrix representations often use linked lists to efficiently store and traverse non-zero elements or connected nodes.

- **Task Scheduling and Process Management**  
  Operating systems use linked lists to manage processes and tasks waiting for execution, as each process can be efficiently added or removed from the schedule.

- **Navigation and Route Management**  
  GPS systems use linked lists to store and manage routes and locations, allowing users to traverse through their journey steps.
- **Implementing Queues and Stacks**  
  Linked lists are commonly used to implement FIFO (First-In-First-Out) queues and LIFO (Last-In-First-Out) stacks, where frequent insertions and deletions at the ends are required. Linked lists provide constant time (O(1)) operations for these use cases, unlike arrays which may require shifting elements.

- **Music and Media Playlists**  
  In music or video players, linked lists manage playlists, allowing easy insertion, deletion, and rearrangement of songs or videos without shifting large blocks of memory.

- **Web Browsing History**  
  Browsers use linked lists to maintain the history of visited pages. The back and forward navigation buttons traverse this linked structure, enabling seamless movement through browsing history.

- **Undo/Redo Functionality**  
  Text editors and graphic design software use linked lists to store user actions. Each action is a node, allowing the application to traverse backward for undo operations and forward for redo operations.

- **Image Viewers**  
  Linked lists organize images, enabling users to move to the next or previous image efficiently, as each image node points to its neighbors.

- **Dynamic Memory Management**  
  Operating systems use linked lists to manage free memory blocks, supporting dynamic allocation and deallocation of memory.

- **File Systems**  
  Many file systems represent directories and files as linked lists, supporting hierarchical navigation and efficient file management.

- **Graph and Sparse Matrix Implementations**  
  Adjacency lists for graphs and sparse matrix representations often use linked lists to efficiently store and traverse non-zero elements or connected nodes.

- **Task Scheduling and Process Management**  
  Operating systems use linked lists to manage processes and tasks waiting for execution, as each process can be efficiently added or removed from the schedule.

- **Navigation and Route Management**  
  GPS systems use linked lists to store and manage routes and locations, allowing users to traverse through their journey steps.



### Implementation of Linked Lists:



```python

# Linked List in Python
class Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class LinkedList:
    def __init__(self):
         self.head = None
         self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for item in reversed(X):
            self.insert_first(item)

    def insert_first(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete_first(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x
    
    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def insert_at(self, i, x):
        if i < 0 or i > len(self):
            raise IndexError("Index out of range")
        if i == 0:
            self.insert_first(x)
            return
        if self.head is None:  
            raise IndexError("Cannot insert at this position in an empty list")
        new_node = Node(x)
        before_node = self.head.later_node(i - 1)
        new_node.next = before_node.next
        before_node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i < 0 or i >= len(self):  
            raise IndexError("Index out of range")
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        return self.delete_at(len(self) - 1)


```
