from collections import deque
from typing import Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    # Use BFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        elif root == []:
            return []
        
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        return root


class Solution2:
    # Use DFS (recursion)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        elif root == []:
            return []
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root