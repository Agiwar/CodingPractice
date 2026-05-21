from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTreeBFS(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        to determine the given two trees are identical or not,
            cuz the structure of node and its value must be the same,
            to visit and compare every nodes across trees,
            using BFS to solve it, (but it doesn't mean layer info matters and required)
            per-node works O(1) time for enqueue and dequeue,
            so total time is O(n) time due to total number of n nodes,
            and space is O(w), w is max width, worst case is O(n)

        time = O(n)
        space = O(w), O(n) worst
        """
        
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        p_queue, q_queue = deque([p]), deque([q])
        
        while p_queue and q_queue:
            p_curr, q_curr = p_queue.popleft(), q_queue.popleft()
            
            if not p_curr and not q_curr:
                continue
            elif p_curr.val != q_curr.val:
                return False
            
            if (
                bool(p_curr.left) != bool(q_curr.left) or
                bool(p_curr.right) != bool(q_curr.right)
            ):
                return False
            
            p_queue.append(p_curr.left)
            p_queue.append(p_curr.right)
            q_queue.append(q_curr.left)
            q_queue.append(q_curr.right)
    
        return not p_queue and not q_queue
    
    def isSameTreeDFS(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        to determine the given two trees are identical or not,
            need to visit every nodes and compare them across two trees,
            so traversal order doesn't matter, but i prefer preorder,
            cuz once the root's values are not matched between two trees,
            program can earlier terminate, if matched, and then can recursive left and right,
            note that the maximum of total number of nodes in tree is 100,
            no recursion stack overflow concerns, so using DFS recursion to solve it,
            when visiting and comparing each node across two trees,
            per-node works O(1) time, and there're n nodes, so O(n) time.

        time = O(n), n is total number of nodes
        space = O(h), recursion typically h = log n, worst case h = n if skewed
        """
        
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (
                p.val == q.val and
                self.isSameTreeDFS(p.left, q.left) and
                self.isSameTreeDFS(p.right, q.right)
            )


isSameTreeBFS = Solution().isSameTreeBFS
isSameTreeDFS = Solution().isSameTreeDFS

def test_isSameTree():
    # LeetCode examples
    # Example 1: p = [1,2,3], q = [1,2,3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTreeBFS(p1, q1) == True

    # Example 2: p = [1,2], q = [1,null,2] -> False
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert isSameTreeBFS(p2, q2) == False

    # Example 3: p = [1,2,1], q = [1,1,2] -> False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTreeBFS(p3, q3) == False

    # Edge cases
    # Both empty
    assert isSameTreeBFS(None, None) == True
    # One empty
    assert isSameTreeBFS(TreeNode(1), None) == False

    # LeetCode examples
    # Example 1: p = [1,2,3], q = [1,2,3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTreeDFS(p1, q1) == True

    # Example 2: p = [1,2], q = [1,null,2] -> False
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert isSameTreeDFS(p2, q2) == False

    # Example 3: p = [1,2,1], q = [1,1,2] -> False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTreeDFS(p3, q3) == False

    # Edge cases
    # Both empty
    assert isSameTreeDFS(None, None) == True
    # One empty
    assert isSameTreeDFS(TreeNode(1), None) == False

    print("All tests passed")


if __name__ == "__main__":
    test_isSameTree()
