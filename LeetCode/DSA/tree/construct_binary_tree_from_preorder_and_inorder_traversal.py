class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        from preorder list, the first num must be a root,
            and check this root is at where in inorder list,
            every nums before this node are left, and every nums after this node are right
            repeating this approach to traverse every node in preorder,
            every node in preorder must always be the root,
            then determine this root's left and right from inorder list

        time = O(n^2), n is preorder.length, and inorder.index
        space = O(n + h), n is creating a tree, h is recursion call
        """
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:(idx + 1)], inorder[:idx])
        root.right = self.buildTree(preorder[(idx + 1):], inorder[(idx + 1):])
        
        return root


buildTree = Solution().buildTree

def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Level-order traversal to list for comparison."""
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

def test_buildTree():
    # LeetCode Example 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] -> [3,9,20,null,null,15,7]
    result = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]

    # LeetCode Example 2: preorder = [-1], inorder = [-1] -> [-1]
    result = buildTree([-1], [-1])
    assert tree_to_list(result) == [-1]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_buildTree()
