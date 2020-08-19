""" 
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

class TreeNode:
  pass

class ListNode:
  pass


def list_of_depths(node: TreeNode) -> ListNode[]:
  """ 
  pseudo:
    - initialize listlist to hold linked lists
    - traverse the binary tree breadth-first, keeping track of level
    - for each level, initialize the first node encountered as the head of a linked list and append the others
    - push the linked list the listlist
    - finally return the listlist
  """

  