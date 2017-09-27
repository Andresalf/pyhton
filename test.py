import datastructures.binarytreeutilities as btutils
from datastructures.binarysearchtree import BinaryTree
from datastructures.binarysearchtree import BinarySearchTree


print("Hello!")
bst = BinarySearchTree()
bst.insert(13)
bst.insert(10)
bst.insert(19)
bst.insert(6)
bst.insert(14)
bst.insert(20)
bst.insert(12)
bst.insert(15)
print(bst.root.data)
print(btutils.get_number_of_leaves(bst.root))
print(btutils.get_printable_tree(bst.root))