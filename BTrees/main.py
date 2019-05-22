from btree import *


tree = BTree(2)

tree.insert(5)
tree.insert(1)
tree.insert(17)
tree.insert(2)
tree.insert(12)
tree.insert(19)
tree.insert(6)
tree.insert(4)
tree.insert(15)

# print(tree)

tree.writeToFile()
tree.readTreeFromFile()

tree.search(14)
tree.search(15)
