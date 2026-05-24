class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_mirror(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return (
            p.val == q.val and
            self._is_mirror(p.left, q.right) and
            self._is_mirror(p.right, q.left)
        )
    
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        if tree is symmetric, root's original left and right become its right and left, respectively
            layer node info doesn't matter, using DFS recursion preorder traversal to visit nodes

        need to traverse all nodes, per-node works O(1) time, so total is O(n) time,
            space is O(h) for recursion, worst case is O(n) if tree is skewed

        time = O(n)
        space = O(h)
        """
        
        return self._is_mirror(root.left, root.right)


isSymmetric = Solution().isSymmetric


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


def test_isSymmetric():
    # LeetCode examples
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])) == True
    assert isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])) == False

    # Edge cases
    # Single node
    assert isSymmetric(TreeNode(1)) == True

    # Same values, asymmetric structure
    assert isSymmetric(build_tree([1, 2, 2, 3, None, 3, None])) == False

    # Deep symmetric tree
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5])) == True

    # Deep mismatch (asymmetry several levels down)
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 9])) == False

    # Symmetric shape, different values at mirrored positions
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 5, 3])) == False

    print("All tests passed")


if __name__ == "__main__":
    test_isSymmetric()
