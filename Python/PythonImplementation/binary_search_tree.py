import argparse
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_search_tree_recursion(root: Optional[TreeNode], target: int) -> bool:
    """
    Check whether target value exists in the BST or not.
    """
    if not root:
        return False
    
    if target > root.val:
        return binary_search_tree_recursion(root.right, target)
    elif target < root.val:
        return binary_search_tree_recursion(root.left, target)
    else:
        return True


def binary_search_tree_iteration(root: Optional[TreeNode], target: int) -> bool:
    if not root:
        return False
    
    while root:
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return True
    
    return False


def insert_recursion(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Insert a new node into the BST.
    """
    if not root:
        return TreeNode(val=val)
    
    if val > root.val:
        root.right = insert_recursion(root.right, val)
    elif val < root.val:
        root.left = insert_recursion(root.left, val)

    return root


def insert_iteration(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    
    curr = root
    while curr:
        if val < curr.val:
            if not curr.left:
                curr.left = TreeNode(val)
                break
            curr = curr.left
        elif val > curr.val:
            if not curr.right:
                curr.right = TreeNode(val)
                break
            curr = curr.right
    
    return root

def find_min_node(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find a min-value node in the BST, the min value is always in the left sub-tree
    """
    curr = root

    while curr and curr.left:
        curr = curr.left
    
    return curr


def remove(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Remove a specific node from a existing BST
    """
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
        
    # target found, and check the current node is leaf or not
    elif not root.left:
        return root.right
    elif not root.right:
        return root.left
    else:
        min_value_node = find_min_node(root.right)
        root.val = min_value_node.val
        root.right = remove(root.right, min_value_node.val)

    return root
