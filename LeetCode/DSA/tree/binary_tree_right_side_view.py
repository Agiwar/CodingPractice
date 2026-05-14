from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        implement BFS layer by layer and visit order is from left to right,
            use queue to store any children of the all node at this layer,
            after each for looping to visit nodes from queue,
            just need to record the rightmost node's value.

        enqueue and dequeue are all O(1) time, and need to do n times (n nodes),
            and access the last one node from queue is O(1) time,
            and space is O(w) w is max width for typical case,
                worst case is O(n) for a completely balanced tree,
                and best case is O(1) for skewed tree,

        time = O(n)
        space = O(w), worst case O(n)
        """
        
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            rightmost_val: int | None = None
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                rightmost_val = curr.val
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            result.append(rightmost_val)
        
        return result


rightSideView = Solution().rightSideView

def test_rightSideView():
    # LeetCode Example 1: root = [1,2,3,null,5,null,4] -> [1,3,4]
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert rightSideView(root) == [1, 3, 4]

    # LeetCode Example 2: root = [1,2,3,4,null,null,null,5] -> [1,3,4,5]
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    assert rightSideView(root) == [1, 3, 4, 5]

    # LeetCode Example 3: root = [1,null,3] -> [1,3]
    assert rightSideView(TreeNode(1, None, TreeNode(3))) == [1, 3]

    # LeetCode Example 4: empty tree -> []
    assert rightSideView(None) == []

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_rightSideView()
