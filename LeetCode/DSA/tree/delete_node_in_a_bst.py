class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _find_min(self, root: TreeNode | None) -> TreeNode | None:
        while root.left:
            root = root.left
        return root
    
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        """
        after deleting the target node with key value, need to keep tree as BST
            to get this, using the right children's node of minimum value to be the root of BST

        so need to implement find a node with minimum value first,
            so that can use this function to get result to be root

        note that there may be zero node in BST, and no any duplicates in BST

        time complexity is O(log n) for finding a minimum, O(log n) for deleting node as well
            where n is total number of nodes in BST

        time = O(log n), the worst case is O(n) due to skewed tree
        space = O(h), h is height of tree due to recursion operation
        """
        
        if not root:
            return None
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif not root.left:
            return root.right
        
        elif not root.right:
            return root.left
        
        else:
            node = self._find_min(root.right)
            root.val = node.val
            root.right = self.deleteNode(root.right, node.val)

        return root


deleteNode = Solution().deleteNode

def inorder(root: TreeNode | None) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def test_deleteNode():
    # LeetCode Example 1: root = [5,3,6,2,4,null,7], key = 3
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = deleteNode(root, 3)
    assert 3 not in inorder(result)
    assert sorted(inorder(result)) == inorder(result)

    # LeetCode Example 2: root = [5,3,6,2,4,null,7], key = 0 (not found)
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = deleteNode(root, 0)
    assert inorder(result) == [2, 3, 4, 5, 6, 7]

    # LeetCode Example 3: empty tree
    assert deleteNode(None, 0) is None

    # Edge cases
    root = TreeNode(5, TreeNode(3), TreeNode(8, TreeNode(6), TreeNode(9)))
    result = deleteNode(root, 5)
    assert inorder(result) == [3, 6, 8, 9]

    print("All tests passed")

if __name__ == "__main__":
    test_deleteNode()
