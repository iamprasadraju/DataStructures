class Node:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, x):
        """Insert x as in a Binary Search Tree."""
        new_node = Node(x)
        if not self.root:
            self.root = new_node
            self.size = 1
            return
        current = self.root
        parent = None
        while current:
            parent = current
            if x < current.item:
                current = current.left
            else:
                current = current.right
        if x < parent.item:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent
        self.size += 1

    def search(self, x):
        """Search for a value x in the tree. Returns the node or None."""
        current = self.root
        while current:
            if x == current.item:
                return current
            elif x < current.item:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left:
                self.inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                self.inorder(node.right)


# Example usage:
tree = BinaryTree()
for val in [10, 5, 15, 2, 7, 12, 20]:
    tree.insert(val)

print("Inorder traversal:")
tree.inorder()  # Output: 2 5 7 10 12 15 20

print("\nSearch for 7:", "Found" if tree.search(7) else "Not found")
print("Search for 100:", "Found" if tree.search(100) else "Not found")




    