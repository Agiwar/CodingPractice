from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        this question is asking how to invert each layer's nodes,
            think about there's a mirror which reflects the inverted root,
            and each node's inversion behaviors have nothing to do with the others,
            which means we don't care about layer's nodes' info,
            e.g., we won't need to collect layer's nodes' values,
            and what traversal doesn't matter either,

        so using DFS recursion swapping root's left and root's right,
            per-node works take O(1) time, and visit n nodes, so O(n) time

        time = O(n), n is number of nodes
        space = O(h) for recursion call, worst case is O(n) for skewed tree
        """

        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root


invertTree = Solution().invertTree


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


def serialize(root: TreeNode | None) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def test_invertTree():
    # LeetCode examples
    assert serialize(invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert serialize(invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]

    # Edge cases
    assert serialize(invertTree(build_tree([]))) == []
    assert serialize(invertTree(build_tree([1]))) == [1]

    print("All tests passed")


if __name__ == "__main__":
    test_invertTree()
