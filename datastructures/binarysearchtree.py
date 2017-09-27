from .binarytree import BinaryTree

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def insert_node(self, root, data):
        if not root:
            root = BSTNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        return root

    def insert(self, data):
        self.root = self.insert_node(self.root, data)
