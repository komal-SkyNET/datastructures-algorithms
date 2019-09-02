import sys
print sys.path
from traversals.traverse import *


class Node:

    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Tree:

    def __init__(self, root):
        self.root = root
"""                    
                    1
            2               3
        4      5        6       7
                     9     10      12
"""

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.right.left = Node(6)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left.left = Node(9)
node.right.left.right = Node(10)
node.right.right.right = Node(12)
tree = Tree(node)

if __name__ == "__main__":
    print 'In order'
    in_order(tree.root)

    print 'Pre order'
    pre_order(tree.root)

    print 'Post order'
    post_order(tree.root)

    print 'Level order'
    level_order(tree.root)