from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def breadth_first_search(root: Optional[TreeNode]) -> None:
    queue = deque()

    if root:
        queue.append(root)
    
    while len(queue) > 0:
        for _ in range(len(queue)):

            curr = queue.popleft()
            print(curr.val)

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
