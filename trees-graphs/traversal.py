class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def insert_many(self, data):
        for i in data:
            self.insert(i)

    def print_tree_inorder(self):
        if self.left:
            self.left.print_tree_inorder()
        print(self.data)
        if self.right:
            self.right.print_tree_inorder()
    
    def print_tree_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_tree_inorder()
        if self.right:
            self.right.print_tree_inorder()

    def print_tree_postorder(self):
        if self.left:
            self.left.print_tree_inorder()
        if self.right:
            self.right.print_tree_inorder()
        print(self.data)


root = Node(1)
root.insert_many([0, 2, 3, 4])
root.print_tree_inorder()