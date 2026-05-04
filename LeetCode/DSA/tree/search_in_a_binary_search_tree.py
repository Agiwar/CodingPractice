class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        according to the BST's properties, find the target val is in BST or not
            here, using the recursion function call
            to find the correct direction of tree's children

        time = O(log n), n is total number of nodes in tree if tree is balanced, worst case is O(n)
        space = O(h) for recursion stack, h is the height of tree, worst case is O(n)
        """

        
        if not root:
            return None
        
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root
    
    def iterSearchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        we may use iteration approach if the tree is quite large,
            this will save space if space matters,
            where recursion call may cause the stack overflow
            
        time = O(log n), n is total number of nodes in tree if tree is balanced,
            the worst case is O(n)
        space = O(1), cuz no recursion operations
        """
        
        while root:
            if root.val == val:
                return root
            
            root = root.left if root.val > val else root.right
        
        return None


searchBST = Solution().searchBST
iterSearchBST = Solution().iterSearchBST

def test_searchBST():
    # LeetCode Example 1: root = [4,2,7,1,3], val = 2 -> [2,1,3]
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = searchBST(root, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3

    # LeetCode Example 2: root = [4,2,7,1,3], val = 5 -> []
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    assert searchBST(root, 5) == None

    # Edge cases
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = iterSearchBST(root, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3
    
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    assert iterSearchBST(root, 5) == None

    print("All tests passed")

if __name__ == "__main__":
    test_searchBST()
