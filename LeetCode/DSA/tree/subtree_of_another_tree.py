class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return (
            p.val == q.val and
            self._isSameTree(p.left, q.left) and
            self._isSameTree(p.right, q.right)
        )
    
    def isSubTree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        subRoot's whole tree structure is the same with subtree of root,
            this is just visiting the nodes and checking, layer nodes info is not required,
            starts with root, using recursion preorder traversal
            to find out the same root in the subtree root,
            cuz subRoot's maximum total number of nodes is 1000,
            so recursion has no stack overflow concerns,
            once subRoot is matched the subtree of root, directly return True,
            however, the root tree may contain duplicates,
            even if the current subRoot's value checking is same with subtree of root,
            still needed to check whether or not there's a matched subRoot,
            cuz their structures might not be the same,
            so go deeper for left and right to confirm.

        for isSameTree recursion operation, per-node works O(1) time,
            there're m nodes in subRoot, so O(m) time,
            and needed to visit n nodes in root, so time is O(n * m)
            and space complexity costs O(h) recursion function call,
            h = log n typically, h = n in worst case for skewed tree

        time = O(n * m), n is total number of nodes in root, m is total number of nodes in subRoot
        space = O(h), h is tree height, typically h = log n, h = n for skewed tree
        """
        
        if not root:
            return False
        
        return (
            self._isSameTree(root, subRoot) or     # if root matched, true
            self.isSubTree(root.left, subRoot) or  # if not matched, go deeper for left
            self.isSubTree(root.right, subRoot)    # if not matched, go deeper for right
        )


isSubTree = Solution().isSubTree

def test_isSubTree():
    # LeetCode examples
    # Example 1: root = [3,4,5,1,2], subRoot = [4,1,2] -> True
    root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubTree(root1, sub1) == True

    # Example 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] -> False
    root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None)), TreeNode(5))
    sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubTree(root2, sub2) == False

    # Edge cases
    # Single node match (minimum size for both)
    assert isSubTree(TreeNode(1), TreeNode(1)) == True

    # Single node, no match
    assert isSubTree(TreeNode(1), TreeNode(2)) == False

    # Deep match — subRoot found several levels down (guards against shallow-search bugs)
    # root: 1 -> 2 -> 3 -> 4 (left chain), subRoot: 3 -> 4
    deep_root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None), None), None)
    deep_sub = TreeNode(3, TreeNode(4), None)
    assert isSubTree(deep_root, deep_sub) == True

    # Duplicate values in root — first match by value isn't structural match,
    # but a later occurrence is. Forces search to keep going after a value hit.
    # root: 1 -> (1, 1 -> 2), subRoot: 1 -> 2
    dup_root = TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(2), None))
    dup_sub = TreeNode(1, TreeNode(2), None)
    assert isSubTree(dup_root, dup_sub) == True

    # Same values, different structure — should NOT match
    # root has subtree [1, 2, null], subRoot is [1, null, 2]
    shape_root = TreeNode(1, TreeNode(2), None)
    shape_sub = TreeNode(1, None, TreeNode(2))
    assert isSubTree(shape_root, shape_sub) == False

    print("All tests passed")

if __name__ == "__main__":
    test_isSubTree()
