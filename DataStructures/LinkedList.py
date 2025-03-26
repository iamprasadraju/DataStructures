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






"""

What is a Linked-List ? -> Sequence x Structure
---------------------

    A Linked list is a linear x structure in which elements (called nodes) are connected using pointers. Unlike arrays, linked lists do not store elements in contiguous memory locations.

Node -> x & *Next Pointer (None)

(HEAD) | item | *next | -> | item | *next | ->  | item | *next | ->  | item | *next | -> | None | 


Linkedlist Interface :
_____________________

. build(iter) --> Creates a Linked list from an iterable -> O(n)

. get_at(i: index) --> Returns the element at given index -> 0(i) : Traverses

. set_at(x, i: index) --> Updates the value at index i with x. -> O(i)

. insert_first(x) --> Inserts a new node at the beginning of the list. -> O(1)

. delete_first() --> Removes the first node from the list and return node.item -> O(1)

. insert_at(x, i:index) --> inserts x at index i -> O(i)

. delete_at(i: index) --> Removes the node at index i and return node.item  ->  O(i)

. insert_last(x) --> insert x at the end of the linkedlist -> O(n)

. delete_last() --> Remove the last node from the linkedlist and return node.item -> O(n)


Where to Use Linked lists ?
_________________________


A Linked list is useful when you need efficienr insertions, deletions, or dynamic resizing.
it is preferred over arrays in scenarios where frequent modifications occurs.





"""








