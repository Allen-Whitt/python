from binaryTreeClass import Node

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.right = Node(0)
root.right.left  = Node(1)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

"""
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
a = 0
def isUniVal(n):
    if n.left == None and n.right == None:
        return True
    elif n.left.data == n.right.data and n.right.data == n.data:
        return True
    return False

def iterTree(r):
    global a
    if isUniVal(r):
        a += 1 
    if r.left:
        iterTree(r.left)
    if r.right:
        iterTree(r.right)

iterTree(root)
print(a) 
