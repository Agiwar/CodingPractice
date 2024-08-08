import argparse
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_search_tree(root: Optional[TreeNode], target: int) -> bool:
    if not root:
        return False
    
    if target > root.val:
        return binary_search_tree(root.right, target)
    elif target < root.val:
        return binary_search_tree(root.left, target)
    else:
        return True
