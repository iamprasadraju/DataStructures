# Stack

A stack is a linear data structure that operates on the Last In, First Out (LIFO) principle. This means the most recently added element is the first one to be removed. All insertions and deletions occur at one end, known as the top of the stack.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Tallrik_-_Ystad-2018.jpg/250px-Tallrik_-_Ystad-2018.jpg)



### Implementation:


Stacks can be implemented using:

- **Arrays**: Provides fast access but has a fixed size.

- **Linked Lists**: Allows dynamic sizing; each new element becomes the new top


## Key Characteristics:

- **Last In, First Out (LIFO) Principle**  
  The defining feature of a stack is that the last element added (pushed) is the first one to be removed (popped). This order is crucial for scenarios where the most recent item needs to be accessed or processed first.

- **Single Access Point (Top of Stack)**  
  All stack operations—push, pop, and peek—are performed at one end, called the "top." This means you can only access or modify the top element directly, not any element in the middle or bottom.

- **Efficient Operations**  
  Push, pop, and peek operations are typically performed in constant time, O(1), making stacks highly efficient for adding and removing elements at the top.

- **Order Preservation**  
  Stacks preserve the order of insertion so that the sequence of removal is always the reverse of the sequence of insertion.

- **Limited Access**  
  Only the top element is accessible at any time. You cannot directly access elements deeper in the stack without popping elements above them.

- **Dynamic or Fixed Size**  
  Stacks can be implemented with a fixed size (using arrays) or with dynamic size (using linked lists), allowing flexibility based on memory and application requirements.

- **Overflow and Underflow Conditions**  
  - **Overflow**: Occurs when pushing onto a full fixed-size stack.  
  - **Underflow**: Occurs when popping from an empty stack.


## Stack Interface:

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lifo_stack.svg/500px-Lifo_stack.svg.png)

- `push(E item)` -> Adds an element to the top of the Stack. --> O(1)

- `pop()` -> Removes the top element from the Stack. --> O(1)

- `peek()` -> Returns the top element without removing it. --> O(1)

- `isEmpty()` -> Checks if the stack is empty. -> boolean --> O(1)

- `size()` -> Returns the number of elements in the Stack. -> int --> O(1)

- `push(E item)` -> Adds an element to the top of the Stack. --> O(1)

- `pop()` -> Removes the top element from the Stack. --> O(1)

- `peek()` -> Returns the top element without removing it. --> O(1)

- `isEmpty()` -> Checks if the stack is empty. -> boolean --> O(1)

- `size()` -> Returns the number of elements in the Stack. -> int --> O(1)

## Where to use Stack:

Stacks are widely used in computer science and software development due to their Last-In, First-Out (LIFO) behavior. Here are the most common and important applications:

- **Function Call Management**  
  Stacks are used to keep track of active function calls in most programming languages. Each time a function is called, its state (local variables, return address) is pushed onto the call stack. When the function returns, its state is popped, ensuring correct program execution flow.

- **Undo/Redo Functionality**  
  Applications like text editors and image editors use two stacks to manage undo and redo operations. Each user action is pushed onto the undo stack, and when undone, it is moved to the redo stack, allowing users to revert or reapply changes easily.

- **Browser Navigation (Back/Forward Buttons)**  
  Web browsers use stacks to manage navigation history. The back stack stores previously visited pages, and the forward stack keeps track of pages navigated away from, enabling smooth back and forward navigation.

- **Expression Evaluation and Conversion**  
  Stacks are crucial for evaluating and converting arithmetic expressions, such as infix to postfix (Reverse Polish Notation) or prefix notation. They help maintain the correct order of operations and handle nested expressions.

- **Syntax Parsing and Parenthesis Matching**  
  Compilers and interpreters use stacks to check whether parentheses, brackets, and braces are correctly matched and nested in code, ensuring code validity.

- **Memory Management**  
  Stacks are used in memory management for allocating and deallocating memory for local variables and function calls, especially in low-level programming and operating systems.

- **Backtracking Algorithms**  
  Stacks support backtracking in algorithms such as maze solving, depth-first search (DFS) in graphs, and puzzle solving. They help keep track of previous states or moves to explore alternative solutions.

- **Task Scheduling and Process Management**  
  Operating systems and multitasking environments use stacks to manage the execution state of tasks and processes, enabling efficient context switching.

- **Other Applications**  
  - Expression matching (validating brackets in code or mathematical expressions)  
  - Reversing data (e.g., reversing a string or sequence)  
  - Implementing recursion (storing recursive function calls and their states)


### Implementation of Stack:


```python
# Stack in Python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """String representation of the stack."""
        return str(self.items)


```