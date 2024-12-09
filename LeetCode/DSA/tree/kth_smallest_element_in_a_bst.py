from typing import List, Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode], res: List[int]) -> List[int]:
            if not root:
                return None
            
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        
        res = []
        inorder(root, res)
        
        return res[k - 1]
