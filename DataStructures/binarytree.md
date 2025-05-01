# Binary Tree


A Binary tree is a hierarchical data structure in which each node has at most two children, commonly referred to as the left child and the right child. This restriction distinguishes binary trees from general trees, where nodes can have any number of children.


![img](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Binary_tree_v2.svg/250px-Binary_tree_v2.svg.png)



## Key Characteristics:


1. **Node Structure:** Each node typically contains a data item, a reference to the left child, and a reference to the right child.


2. **Root Node:** The topmost node from which the tree hierarchy begins.


3. **Leaf Nodes:** Nodes without any children, representing the terminal points of the tree.


4. **Subtree:** Any node and its descendants form a subtree, which itself is a binary tree.



## Types of Binary Trees



```markdown
# 🌲 Types of Binary Trees – Definitions & Key Characteristics

This document outlines the **main types of binary trees**, their **defining features**, **properties**, and **examples**.

---

## 1. Full Binary Tree

- **Definition**: A binary tree in which every node has **either 0 or 2 children**.

- **Properties**:
  - Internal (non-leaf) nodes always have two children.
  - A non-empty full binary tree with `I` internal nodes has `L = I + 1` leaves.
  
- **Example**:
  ```
      1  
     / \  
    2   3  
   / \     
  4   5
  ```

---

## 2. Perfect Binary Tree

- **Definition**: A binary tree in which **all internal nodes have two children**, and **all leaves are at the same level**.
- **Properties**:
  - Total nodes: `2^(h+1) - 1` for height `h`.
  - Always both **full** and **complete**.
- **Example**:
  ```
      1  
     / \  
    2   3  
   / \ / \  
  4  5 6  7
  ```

---

## 3. Complete Binary Tree

- **Definition**: A binary tree where **all levels are fully filled except possibly the last**, and the **last level's nodes are left-aligned**.
- **Properties**:
  - Efficiently stored in arrays (e.g., for heaps).
  - Height is minimized.
- **Example**:
  ```
      1  
     / \  
    2   3  
   / \ /  
  4  5 6
  ```

---

## 4. Degenerate (Pathological) Tree

- **Definition**: A binary tree in which each parent has **only one child**, essentially forming a **linked list**.
- **Properties**:
  - Worst-case height: `n` nodes → height = `n - 1`.
  - Occurs with sorted insertions (e.g., 1 → 2 → 3 → 4).
- **Example**:
  ```
  1  
   \  
    2  
     \  
      3  
       \  
        4
  ```

---

## 5. Balanced Binary Tree

- **Definition**: A binary tree where the **height difference between left and right subtrees of every node is ≤ 1**.
- **Purpose**: Maintains `O(log n)` time for operations like search, insert, and delete.
- **Examples**:
  - **AVL Tree**
  - **Red-Black Tree**

---

## 🎯 Specialized Binary Trees

- **Binary Search Tree (BST)**:  
  - Rule: `Left < Root < Right`  
  - Enables efficient search, insert, and delete (`O(log n)` average case).

- **Strictly Binary Tree**:  
  - Every non-leaf node has **exactly two children** (same as full binary tree).

- **Heap**:
  - A **complete binary tree** satisfying the **heap-order property**:
    - **Min-Heap**: Parent ≤ Children  
    - **Max-Heap**: Parent ≥ Children

---

## 📊 Key Differences Table

| Type            | Node Children       | Leaf Depth     | Primary Use Case               |
|------------------|---------------------|----------------|--------------------------------|
| **Full**         | 0 or 2              | Varies         | Decision-making algorithms     |
| **Perfect**      | All internal: 2     | Same           | Theoretical modeling           |
| **Complete**     | Last level: left-aligned | Varies   | Priority queues, heaps         |
| **Degenerate**   | 1 per node          | `O(n)`         | Worst-case BST, linked list    |
| **Balanced**     | Height balanced     | Nearly equal   | Efficient searching/insertion  |

---

### 🔁 Relationship Notes

- **Perfect ⇒ Full & Complete**  
- **Full ≠ Complete**: A full tree doesn’t require nodes to be left-aligned.
- **Degenerate ⊆ BST** (if sorted insertions are used)

---



