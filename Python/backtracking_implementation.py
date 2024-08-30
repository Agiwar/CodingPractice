from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right= right


def can_reach_leaf(root: Optional[TreeNode]) -> bool:
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    
    if can_reach_leaf(root.left):
        return True
    
    if can_reach_leaf(root.right):
        return True
    
    return False


def leaf_path(root: Optional[TreeNode], path: List) -> bool:
    if not root or root.val == 0:
        return False
    
    path.append(root.val)

    if not root.left and not root.right:
        return True
    
    if leaf_path(root.left):
        return True
    
    if leaf_path(root.right):
        return True
    
    path.pop()

    return False