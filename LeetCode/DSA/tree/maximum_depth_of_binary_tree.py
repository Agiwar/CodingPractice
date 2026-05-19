class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        find a tree's maximum depth, using DFS to recursively function call,
            to get the tree's depth, apply bottom-up approach to aggregate the depth results
            go for postorder traversal to determine the each single's way's depth,
            and per-node works O(1) time, needed to visit n nodes, so O(n) time,
            as space, O(h) typically, worst case is O(n) for skewed tree

        time = O(n), n is total number of nodes
        space = O(h), h is for recursion call
        """

        
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1


maxDepth = Solution().maxDepth


def build_tree(values: list) -> TreeNode | None:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def test_maxDepth():
    # LeetCode examples
    assert maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert maxDepth(build_tree([1, None, 2])) == 2

    # Edge cases
    assert maxDepth(build_tree([])) == 0
    assert maxDepth(build_tree([1])) == 1

    print("All tests passed")


if __name__ == "__main__":
    test_maxDepth()
