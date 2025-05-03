# 1. Binary Node (Base Node Class)
class Binary_Node:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None

    def subtree_iter(self):
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        return self

    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        return self

    def successor(self):
        if self.right:
            return self.right.subtree_first()
        node = self
        while node.parent and node is node.parent.right:
            node = node.parent
        return node.parent

    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        node = self
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def subtree_insert_before(self, B):
        if self.left:
            last = self.left.subtree_last()
            last.right, B.parent = B, last
        else:
            self.left, B.parent = B, self

    def subtree_insert_after(self, B):
        if self.right:
            first = self.right.subtree_first()
            first.left, B.parent = B, first
        else:
            self.right, B.parent = B, self

    def subtree_delete(self):
        if self.left or self.right:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
        return self

# 2. BST Node (Extends Binary_Node)
class BST_Node(Binary_Node):
    def subtree_find(self, k):
        if k < self.item['key']:
            return self.left.subtree_find(k) if self.left else None
        elif k > self.item['key']:
            return self.right.subtree_find(k) if self.right else None
        return self

    def subtree_find_next(self, k):
        if self.item['key'] <= k:
            return self.right.subtree_find_next(k) if self.right else None
        else:
            B = self.left.subtree_find_next(k) if self.left else None
            return B if B else self

    def subtree_find_prev(self, k):
        if self.item['key'] >= k:
            return self.left.subtree_find_prev(k) if self.left else None
        else:
            B = self.right.subtree_find_prev(k) if self.right else None
            return B if B else self

    def subtree_insert(self, B):
        if B.item['key'] < self.item['key']:
            if self.left:
                self.left.subtree_insert(B)
            else:
                self.subtree_insert_before(B)
        elif B.item['key'] > self.item['key']:
            if self.right:
                self.right.subtree_insert(B)
            else:
                self.subtree_insert_after(B)
        else:
            self.item = B.item  # Update existing key

# 3. Binary Tree Wrapper
class Binary_Tree:
    def __init__(self, Node_Type=Binary_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root:
            for node in self.root.subtree_iter():
                yield node.item

# 4. Set Binary Tree (Binary Search Tree with Set Interface)
class Set_Binary_Tree(Binary_Tree):
    def __init__(self):
        super().__init__(BST_Node)

    def iter_order(self):
        yield from self

    def find_min(self):
        return self.root.subtree_first().item if self.root else None

    def find_max(self):
        return self.root.subtree_last().item if self.root else None

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            return node.item if node else None

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            return node.item if node else None

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            return node.item if node else None

    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None:
                return False
        else:
            self.root = new_node
        self.size += 1
        return True

    def delete(self, k):
        if not self.root:
            return None
        node = self.root.subtree_find(k)
        if not node:
            return None
        removed = node.subtree_delete()
        if removed.parent is None:
            self.root = None
        self.size -= 1
        return removed.item

    def build_from_sorted_list(self, sorted_items):
        def build_subtree(i, j):
            if i > j:
                return None
            mid = (i + j) // 2
            root = self.Node_Type(sorted_items[mid])
            root.left = build_subtree(i, mid - 1)
            if root.left:
                root.left.parent = root
            root.right = build_subtree(mid + 1, j)
            if root.right:
                root.right.parent = root
            return root

        self.root = build_subtree(0, len(sorted_items) - 1)
        self.size = len(sorted_items)



tree = Set_Binary_Tree()
data = [{'key': k} for k in [1, 3, 5, 7, 9]]
tree.build_from_sorted_list(data)

print("In-order Traversal:")
for item in tree.iter_order():
    print(item)

print("Find key 5:", tree.find(5))
print("Find next after 5:", tree.find_next(5))
print("Delete key 5:", tree.delete(5))

print("After deletion:")
for item in tree.iter_order():
    print(item)
