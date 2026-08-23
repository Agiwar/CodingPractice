class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        first number from preorder must be root node, and the others are also root node of subtree,
        create a hashmap to store the index of each root node value from inorder
        
        time = O(n), traverse preorder and inorder
        space = O(n), create hashmap
        """
        
        node_idx_inorder = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)
        
        def build(left_bound: int, right_bound: int) -> TreeNode | None:
            if left_bound > right_bound:
                return None
            
            node_val = next(preorder_iter)
            node = TreeNode(node_val)
            
            node_idx = node_idx_inorder[node_val]
            
            node.left = build(left_bound, node_idx - 1)
            node.right = build(node_idx + 1, right_bound)
            
            return node
        
        return build(0, len(preorder) - 1)


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

    print("All tests passed")


if __name__ == "__main__":
    test_buildTree()
