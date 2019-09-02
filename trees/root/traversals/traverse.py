from tree import Node, Tree
from collections import deque

# L, Root, R
def in_order(node):
    if node.left:
        in_order(node.left)
    print node.val
    if node.right:    
        in_order(node.right)

# Root, L, R
def pre_order(node):
    print node.val
    if node.left:
        in_order(node.left)
    if node.right:    
        in_order(node.right)

#L, R, Root
#Print leaves before ROOT
def post_order(node):
    if node.left:
        in_order(node.left)
    if node.right:    
        in_order(node.right)
    print node.val

def level_order(node):
    queue = deque([node])
    while (len(queue)>0):
        cur_node = queue.popleft()
        print cur_node.val
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
        
