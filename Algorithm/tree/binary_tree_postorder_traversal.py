from typing import List, Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        def postorder(root: Optional[TreeNode], res: List[int]) -> List[int]:
            if not root:
                return None
            
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)
        
        
        output = []
        postorder(root, output)
        return output