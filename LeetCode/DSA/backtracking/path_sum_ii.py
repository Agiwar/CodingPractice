class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        """
        collect every root-to-leaf path whose values sum to targetSum
        a path is a solution exactly when it ends at a leaf and remaining is zero

        the DFS helper returns nothing: it mutates shared state,
            base case is no node, just return
            path is shared and mutated by backtracking, so each match is stored as a copy

        time = O(n + s * h), traversal is O(n), but copying a found path costs O(h),
                n is total number of nodes, s is number of solution paths (at most number of leaves),
                h is the height of the tree,
                a full tree where every leaf matches gives O(n log n),
                the true worst case is O(n^2): a chain ending in a bush, all zeros with target 0,
                every solution path drags the whole chain with it
        space = O(h) for recursion stack and the current path,
                the output itself duplicates shared prefixes (root value appears in every copied path),
                so it holds s * h values, up to O(n^2) in the worst case
        """
        
        output: list[list[int]] = []
        path: list[int] = []
        
        def collect_paths(node: TreeNode | None, remaining: int) -> None:
            if not node:
                return
            
            path.append(node.val)
            remaining -= node.val
            
            if not node.left and not node.right and remaining == 0:
                output.append(path.copy())
            
            collect_paths(node.left, remaining)
            collect_paths(node.right, remaining)
            
            path.pop()
        
        collect_paths(root, targetSum)
        return output


pathSum = Solution().pathSum

def test_pathSum():
    # LeetCode Example 1: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 -> [[5,4,11,2],[5,8,4,5]]
    root = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    )
    assert pathSum(root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]

    # LeetCode Example 2: root = [1,2,3], targetSum = 5 -> []
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert pathSum(root, 5) == []

    # LeetCode Example 3: root = [1,2], targetSum = 0 -> []
    root = TreeNode(1, TreeNode(2))
    assert pathSum(root, 0) == []

    # Edge cases
    # empty tree -> []
    assert pathSum(None, 0) == []

    # single node, matches -> [[1]]
    assert pathSum(TreeNode(1), 1) == [[1]]

    # single node, does not match -> []
    assert pathSum(TreeNode(1), 0) == []

    # target reached at an internal node, but it is not a leaf -> []
    assert pathSum(TreeNode(1, TreeNode(2)), 1) == []

    # left path fails, right path succeeds -> the left path must be undone first
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert pathSum(root, 4) == [[1, 3]]

    # two distinct leaves produce the same path values -> both are reported
    root = TreeNode(1, TreeNode(2), TreeNode(2))
    assert pathSum(root, 3) == [[1, 2], [1, 2]]

    # running sum dips negative and recovers -> no early pruning allowed
    root = TreeNode(1, TreeNode(-2, TreeNode(3)))
    assert pathSum(root, 2) == [[1, -2, 3]]

    # left-skewed chain
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert pathSum(root, 6) == [[1, 2, 3]]

    print("All tests passed")

if __name__ == "__main__":
    test_pathSum()
