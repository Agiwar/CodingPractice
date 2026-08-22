class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _subtree_height(self, node: TreeNode | None) -> int:
        """
        check the height of the node's subtree which has left and right,
            the number of left children may be different from rights',
            so the node height is from the maximum height of left subtree or right's,
            and then plus one
        
        the base case is when there's no node, height is zero, leaf node has height of one,
            postorder traverse the tree node, if one of the subtree is already imbalanced,
            then whole tree must be imbalanced, otherwise, needed to continue checking the others
            also, imbalanced means the difference of node's left and right subtree heights is greater than one

        return -1 to tell the caller it's already imbalanced,
            it's safe because a real height is never negative

        time = O(n), each node does O(1) work, total nodes is n, so O(n)
        space = O(h), h is height of tree due to recursion call stack
        """

        if not node:
            return 0

        left_height = self._subtree_height(node.left)
        right_height = self._subtree_height(node.right)

        if (
            left_height == -1 or
            right_height == -1 or
            abs(left_height - right_height) > 1
        ):
            return -1

        return max(left_height, right_height) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self._subtree_height(root) != -1


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
    # single node -> True
    assert isBalanced(TreeNode(1)) is True

    # two nodes, height diff of exactly 1 -> True (boundary, must not be rejected)
    assert isBalanced(TreeNode(1, TreeNode(2))) is True

    # left-skewed chain of 3 -> False (imbalance detected below the root)
    assert isBalanced(TreeNode(1, TreeNode(2, TreeNode(3)))) is False

    # right-skewed chain of 3 -> False (mirror of the above)
    assert isBalanced(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) is False

    # balanced at the root, imbalanced deep inside the left subtree -> False
    #           1
    #         /   \
    #        2     3        node 2: left height 2, right height 0 -> imbalanced
    #       /       \       root:   left height 3, right height 3 -> looks fine
    #      4         5
    #     /           \
    #    6             7
    root = TreeNode(1,
        TreeNode(2, TreeNode(4, TreeNode(6))),
        TreeNode(3, None, TreeNode(5, None, TreeNode(7)))
    )
    assert isBalanced(root) is False

    print("All tests passed")

if __name__ == "__main__":
    test_isBalanced()
