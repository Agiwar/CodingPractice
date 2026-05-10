class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _tree_height_diff(self, root: TreeNode | None) -> int:
        """
        in order to determine the tree (or subtree) is balanced,
            need to calculate the left height and right's,
            we can then calculate the height diff from left and right,
            so go the postorder traversal, calculate left height first and then right's,

        a single node has no height which is zero, this is base case
            height is defined as root -> root.left or root.right,
            if subtree is imbalanced, then whole tree is definitely imbalanced,
            if subtree is balanced, still need to check the rest of tree (the other subtree) balance status

        from balanced definition, it means abs(left - right) > 1,
            so left > 1 + right or right > 1 + left,
            this derives that left and right must be always positive integer

        time = O(n), n is total number of tree nodes
        space = O(h), h is height of tree due to recursion call
        """
        
        if not root:
            return 0
        
        left_height = self._tree_height_diff(root.left)
        right_height = self._tree_height_diff(root.right)
        
        if (
            left_height == -1 or
            right_height == -1 or
            abs(left_height - right_height) > 1
        ):
            return -1
        
        return max(left_height, right_height) + 1

    
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        return self._tree_height_diff(root) != -1


isBalanced = Solution().isBalanced

def test_isBalanced():
    # LeetCode Example 1: root = [3,9,20,null,null,15,7] -> True
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert isBalanced(root) is True

    # LeetCode Example 2: root = [1,2,2,3,3,null,null,4,4] -> False
    root = TreeNode(1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2)
    )
    assert isBalanced(root) is False

    # LeetCode Example 3: empty tree -> True
    assert isBalanced(None) is True

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_isBalanced()
