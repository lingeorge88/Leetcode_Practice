class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val

# search a node given the root of a bst
def search(root, target):
    if root == None:
        return False
    
    if root.val > target:
        search(root.left, target)
    elif root.val < target:
        search(root.right, target)
    else:
        return True

# insert a new node and return the root of the bst
def insert(root, val):
    if root == None:
        return TreeNode(val)

    if val > root.val:
        insert(root.right, val)
    elif val < root.val:
        insert(root.left, val)
    
    return root

# return the minimum value of a BST given the root
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    
    return curr

# remove a node and return the root of a BST
def remove(root, val):
    if not root:
        return None

    # find the node to remove
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.left:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    
    return root