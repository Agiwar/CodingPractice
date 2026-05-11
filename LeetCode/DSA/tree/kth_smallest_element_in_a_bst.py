class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        find the kth smallest node, need the inorder traversal to visit all nodes,
            and the kth smallest node will be the kth nodes during inorder traversal

        time = O(h + k) is cuz do left traversal first which is O(h),
            and then go back root to check whether or not this root is the kth root,
            so time is O(k), overall is O(h + k),
            and if k is the last node from BST, so need to visit all nodes from BST,
            so time = O(n) not O(h) due to all traversal not half sideways, and now k is n, O(n + n) = O(n)


        time = O(h + k), O(n) worst case
        space = O(h), h is stack.length means which one way we go
        """
        
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            
            if k == 0:
                return curr.val
            
            curr = curr.right



kthSmallest = Solution().kthSmallest

def test_kthSmallest():
    # LeetCode Example 1: root = [3,1,4,null,2], k = 1 -> 1
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kthSmallest(root, 1) == 1

    # LeetCode Example 2: root = [5,3,6,2,4,null,null,1], k = 3 -> 3
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert kthSmallest(root, 3) == 3

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_kthSmallest()
