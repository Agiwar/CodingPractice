class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============ Search ============

def search(root: TreeNode | None, target: int) -> bool:
    """
    Check whether target value exists in the BST.
    
    time: O(log n) balanced, O(n) worst
    space: O(h) recursion stack
    """
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


def search_iter(root: TreeNode | None, target: int) -> bool:
    """
    Iterative search — preferred when stack space matters.
    
    time: O(log n) balanced, O(n) worst
    space: O(1)
    """
    while root:
        if root.val == target:
            return True
        root = root.left if target < root.val else root.right
    
    return False


# ============ Insert ============

def insert(root: TreeNode | None, val: int) -> TreeNode:
    """
    Insert a new node into the BST. Returns the root.
    Duplicates are ignored.
    
    time: O(log n) balanced, O(n) worst
    space: O(h) recursion stack
    """
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    # val == root.val: duplicate, do nothing
    
    return root


def insert_iter(root: TreeNode | None, val: int) -> TreeNode:
    """
    Iterative insert — preferred when stack space matters.
    
    time: O(log n) balanced, O(n) worst
    space: O(1)
    """
    new_node = TreeNode(val)
    
    if not root:
        return new_node
    
    curr = root
    while True:
        if val < curr.val:
            if not curr.left:
                curr.left = new_node
                break
            curr = curr.left
        elif val > curr.val:
            if not curr.right:
                curr.right = new_node
                break
            curr = curr.right
        else:
            # duplicate, do nothing
            break
    
    return root


# ============ Remove ============

def find_min(root: TreeNode) -> TreeNode:
    """
    Find the minimum node in a subtree.
    The min is always the leftmost node.
    
    time: O(h)
    space: O(1)
    """
    while root.left:
        root = root.left
    return root


def remove(root: TreeNode | None, val: int) -> TreeNode | None:
    """
    Remove a node with given value from the BST. Returns the root.
    
    Three cases when node is found:
        1. Leaf node: just remove
        2. One child: replace with child
        3. Two children: replace with inorder successor (min of right subtree)
    
    time: O(log n) balanced, O(n) worst
    space: O(h) recursion stack
    """
    if not root:
        return None

    # Search phase
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # Found — handle removal
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Two children: replace with inorder successor
        successor = find_min(root.right)
        root.val = successor.val
        root.right = remove(root.right, successor.val)

    return root
