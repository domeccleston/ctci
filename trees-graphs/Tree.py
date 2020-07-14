"""
NOTES

tree: 
    - a data structure made of nodes
    - each tree has a root node*
    - the root node has 0 or more children
    - the children have 0 or more children

binary tree: each node has up to two children

leaf: a node with no children

binary search tree: 
    - for each node n, all left descendants <= n < all right descendants**
    - don't assume that the binary tree specified is a binary search tree

balanced vs unbalanced binary trees:
    - complete: every level of the tree is filled, except possibly the last
    - full: every node has 0 or 2 children
    - perfect: full + complete


*  not necessarily true in graph theory, but this is how we use trees in this context
** this puts duplicates on the left; some definitions prohibit duplicates, some put duplicates on the right.
   check this with interviewer

"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


