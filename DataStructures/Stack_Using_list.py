class Stack(): 

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        del self.stack[-1]
    
    def peek(self):
        return self.stack[-1]

        
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack[::-1])
    


"""

What is a Stack ? --> Sequence Data structure
----------------

    A Stack is a fundamental data structure that follows the Last-In, First-Out (LIFO) principle, meaning the last element added is the first one removed.


Stack Interface --> Operations
----------------

. push(E item) -> Adds an element to the top of the Stack. --> O(1)

. pop() -> Removes the top element from the Stack. --> O(1)

. peek() -> Returns the top element without removing it. --> O(1)

. isEmpty() -> Checks if the stack is empty. -> boolean --> O(1)

. size() -> Returns the number of elements in the Stack. -> int --> O(1)


Applications of Stack:
----------------------

. Function call Stack -> Stacks are Used to manage function calls in programming languages , keeping track of the order in which functions are called.

. Backtracking Algorithm -> Stacks can be used to implement backtracking algorithmsm, Where you explore different paths in a problem space.

. Expression Evaluation -> Stacks are used to evalute mathematical expressions, especially those with parentheses.

. Memory Management -> Stacks are used for managing memory allocation and deallocation.


Anology of Stack:
----------------
A Stack can be visualized as a pile of pancakes, where you can only add or remove pancakes from the top.


"""


























