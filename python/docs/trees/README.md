# Trees

Trees are an important variation of the graph data structure. They consist of nodes and edges. The topmost node is called the root. Nodes typically hold a value and then a varying number of pointers to 'child' nodes. The bottomost nodes have no children and are referred to as leaves.

A binary tree is a type of tree wherein each node only has up to 2 children: left or right.
A special variation of the binary tree is the binary search tree wherein the insertion of nodes is adjusted such that the left node only receives values which are less than the root and the right node only receives values which are greater than the root.

## Challenge
Implement a binary tree.
- It should have methods for preorder, in-order, and postorder traversal.
- Each of these methods should return an array of the node values.

Implement a binary search tree (BST).
- It should have an add method.
- It should have a contains method.

## Approach & Efficiency

A recursive approach was taken for all methods.

Efficiency:
- Time -> O(2^d) where d is the depth of the tree for all binary tree methods since each node must be visited in the traversal. For the binary search tree contains and add are run in O(log(n)) where n is the number of nodes because the tree is sorted and the possible nodes to visit are halved on each recursive call.
- Space -> O(1) since all methods only use pointers and thus memory used is not proportional to the number of calls.


## API

**Binary Tree**

- Preorder traversal -> node values are added to the return array in order of root -> left -> right
- Preorder traversal -> node values are added to the return array in order of left -> root -> right
- Preorder traversal -> node values are added to the return array in order of right -> left -> root

**Binary search tree**
- Add -> adds nodes to the tree by following the principal of adding values less than the root to the left child and those greater than the root to the right child.
- Contains -> Returns true if a value is contained in the tree, false if not.
