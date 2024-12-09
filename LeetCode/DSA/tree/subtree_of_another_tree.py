from typing import Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def is_same_tree(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and not r2:
            return True
        
        elif not r1 or not r2:
            return False
        
        return (
            r1.val == r2.val and
            Solution.is_same_tree(r1.left, r2.left) and 
            Solution.is_same_tree(r1.right, r2.right)
        )

    @staticmethod
    def find_node_match(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1:
            return False
        
        elif Solution.is_same_tree(r1, r2):
            return True
        
        return Solution.find_node_match(r1.left, r2) or Solution.find_node_match(r1.right, r2)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return Solution.find_node_match(root, subRoot)