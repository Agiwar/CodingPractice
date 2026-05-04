class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        to insert a value into a BST, and it guarantees the given value doesn't exist the in the BST,
            after insertion, we need to keep the BST

        time = O(log n), n is total number of tree nodes, worst case is O(n) is tree is skewed
        space = O(h), h is height of BST due to recursion function call
        """
        
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
    
    def iterInsertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        using iteration approach to insert the val into BST,
            if BST is a larch-tree, iteration can avoid recursion stack overflow
        
        time = O(log n), n is total number of nodes in BST, worst case is O(n) due to skewed
        space = O(1), no recursion operations
        """
        
        node = TreeNode(val)
        
        if not root:
            return node
        
        curr = root
        while curr:
            if curr.val > val:
                if not curr.left:
                    curr.left = node
                    break
                curr = curr.left
            
            elif curr.val < val:
                if not curr.right:
                    curr.right = node
                    break
                curr = curr.right
        
        return root
                


insertIntoBST = Solution().insertIntoBST
iterInsertIntoBST = Solution().iterInsertIntoBST


def inorder(root: TreeNode | None) -> list[int] | None:
    """
    convert the tree node to a list
    """
    
    return inorder(root.left) + [root.val] + inorder(root.right) if root else[]


def test_insertIntoBST():
    # LeetCode Example 1: root = [4,2,7,1,3], val = 5
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = insertIntoBST(root, 5)
    assert inorder(result) == [1, 2, 3, 4, 5, 7]

    # LeetCode Example 2: root = [40,20,60,10,30,50,70], val = 25
    root = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70)))
    result = insertIntoBST(root, 25)
    assert inorder(result) == [10, 20, 25, 30, 40, 50, 60, 70]

    # Edge case: empty tree
    result = insertIntoBST(None, 5)
    assert result.val == 5

    # Edge cases
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = iterInsertIntoBST(root, 5)
    assert inorder(result) == [1, 2, 3, 4, 5, 7]

    # LeetCode Example 2: root = [40,20,60,10,30,50,70], val = 25
    root = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70)))
    result = iterInsertIntoBST(root, 25)
    assert inorder(result) == [10, 20, 25, 30, 40, 50, 60, 70]

    # Edge case: empty tree
    result = iterInsertIntoBST(None, 5)
    assert result.val == 5

    print("All tests passed")
    

if __name__ == "__main__":
    test_insertIntoBST()
