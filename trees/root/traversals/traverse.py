from tree import Node, Tree

def in_order(node):
    if node.left:
        in_order(node.left)
    print node.val
    if node.right:    
        in_order(node.right)

def pre_order(node):
    print node.val
    if node.left:
        in_order(node.left)
    if node.right:    
        in_order(node.right)

def post_order(node):
    if node.left:
        in_order(node.left)
    if node.right:    
        in_order(node.right)
    print node.val