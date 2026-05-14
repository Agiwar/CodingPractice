from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        implement BFS, traversal all nodes from level 0 until the last level,
            and traversal order is from left to right,
            use queue for collecting the current node's children if any which exist at next layer,
            and in the for loop, it's a snapshot of current queue's status,
            it means this loop will pop all nodes at this level,
            and make sure the current popped node has left or right children,
            if yes, enqueue them to queue,
            as time complexity, each node will be enqueued and dequeued,
            both enqueue and dequeue via popleft is O(1),
            and there're number of n nodes needed traversal, so total is O(n)
            and space complexity is O(w) in average for balanced tree,
            where w is the max width of a level in tree
            the worst case is O(n) completely balanced tree,
            if root is None, bool(deque([None])) is True, this queue is not empty
    
            time = O(n), n is total number of nodes
            space = O(n) is the worst case, O(w) in average where w is the max width of a level
            """

        
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result


levelOrder = Solution().levelOrder

def test_levelOrder():
    # LeetCode Example 1: root = [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert levelOrder(root) == [[3], [9, 20], [15, 7]]

    # LeetCode Example 2: root = [1] -> [[1]]
    assert levelOrder(TreeNode(1)) == [[1]]

    # LeetCode Example 3: empty tree -> []
    assert levelOrder(None) == []

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_levelOrder()
