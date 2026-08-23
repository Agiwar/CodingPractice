class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    return True if reach the leaf node which has no left nor right children,
        and in this leaf node, if the current targetSum is zero,
        then return True
    
    the main idea is getting started at root, and do DFS,
        each movement decremental targetSum by minus the current node value
        but if not meet the contract (which is at leaf node and current targetSum is zero),
        then the answer path must exists in the others
        so try go to left subtree first and then right subtree
    
    time = O(n), the worst case is we need to traverse all nodes
    space = O(h), h is the height of root due to recursive call
    """
    
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if (
            not root.left and
            not root.right and
            targetSum == 0
        ):
            return True
        
        return (
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
        )

hasPathSum = Solution().hasPathSum

def test_hasPathSum():
    # LeetCode Example 1: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 -> True
    root = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    )
    assert hasPathSum(root, 22) is True

    # LeetCode Example 2: root = [1,2,3], targetSum = 5 -> False
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert hasPathSum(root, 5) is False

    # LeetCode Example 3: empty tree, targetSum = 0 -> False
    assert hasPathSum(None, 0) is False

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_hasPathSum()
