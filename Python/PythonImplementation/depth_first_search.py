from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> None:
    """
    Visit left sub-tree first, then visit root, and finally visit right sub-tree.
    """
    if not root:
        return None
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root: Optional[TreeNode]) -> None:
    """
    Visit parent root first, then visit left sub-tree, and finally visit right sub-tree.
    """
    if not root:
        return None
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root: Optional[TreeNode]) -> None:
    """
    Visit left sub-tree first, then visit right sub-tree, and finally visit root.
    """
    if not root:
        return None
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)
