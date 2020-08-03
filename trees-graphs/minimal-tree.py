""" 
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an 
algo­rithm to create a binary search tree with minimal height.

arr = [1, 2, 3, 4, 5]
simple implementation, initialize a binary tree with the first element and add subsequent elements:
        1
         \
          2
           \
            3
             \
              4
               \
                5
but that's maximum height, not minimum. let's see if we can write a shorter tree

            3
          /   \
         2     4
        /       \
       1         5   
starting with the middle element of the array reduced the height to 3 from 5.
could we reduce it further? not in this case, since that would necessitate adding more than
two children two our first node.

can we calculate the size of this tree from the size of the array? let's try an even number of elements
[1, 2, 3, 4, 5, 6]

            3              <- adding to         
          /   \               the above
         2     4             
        /       \
       1         5
                  \
                   6  


            3
          /   \
         2     5
        /     /  \
       1     4    6 


we can remain at height three by shifting the order of the elements.
this makes sense: the way to reduce height is to take advantage of the fact that each node can 
have two children, a smaller child and a larger child. we can't do that if we keep appending nodes
in simple increasing order: that way we end up with the original tree of length n

this has a recursive structure: something like

- take our root node
- look at the content of our array to the left of the node: form it into a binary tree
- look at the content of our array to the right: form it into a binary tree
- append the root nodes of each of our binary trees to our initial binary tree

when we make our sub-trees from the left and right halves, the recursion comes in: we look at the center
element, look at the left and right halves, and form a tree. this hits the base case immediately in
our small example here, because we end up with no more children after one step: 2 -> 1 and 4 -> 5 | 4 -> 6

let me test this with a larger example: [2, 4, 5, 7, 9, 10, 15, 31]

                7
             /     \
            4       10
          /  \     /   \ 
         2    5   9     15
                          \
                           31

"""

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def print_tree(self):
    print(self.data)
    if self.left:
      self.left.print_tree()
    if self.right:
      self.right.print_tree()

  def insert(self, data):
    if self.data:
      if data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
      elif data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
    else:
      self.data = data

def middle_element(arr):
  return (len(arr) - 1) // 2

def minimal_tree(arr: list, parent=None) -> Node:
  index = middle_element(arr)
  left = arr[:index]
  right = arr[index + 1:]

  if len(left) == 0 or len(right) == 0:
    return arr[index]
  else:
    root = Node(arr[index])
    root.insert(minimal_tree(left))
    root.insert(minimal_tree(right))

  return root

  # left_subtree = minimal_tree(left, root)
  # root.print_tree()
  # left_subtree.print_tree()

test0 = [1, 2, 3]
test1 = [1, 2, 3, 4, 5, 6]
test2 = [2, 4, 5, 7, 9, 10, 15, 31]

tree = minimal_tree(test1)
tree.print_tree()