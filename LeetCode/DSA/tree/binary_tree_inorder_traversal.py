class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        traversing the binary tree and print the node's value inorder,
            note that tree is not BST

        time = O(n), n is total number of nodes in tree
        space = O(n) + O(h), where O(n) is creating a list, O(h) is recursion call, h is height of tree
        """

        
        if not root:
            return []
        
        return (
            self.inorderTraversal(root.left) +
            [root.val] +
            self.inorderTraversal(root.right)
        )
    
    def iterInorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        using iteration to do inorder traversal, where there's no recursion operations,
            duration traversal, need to record every node we seen, and push it into stack,
            first go left, until exhausted, pop from stack which is the next node to visit,
            record its value, then go to its right child.
            and checking this parent has right or not, and continuing this progress

        time = O(n), n is total number of nodes in tree
        space = O(n) for creating result, and O(h) is storing the nodes where path we go
        """
        
        stack = []
        inorder = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            inorder.append(curr.val)
            
            curr = curr.right
        
        return inorder


inorderTraversal = Solution().inorderTraversal
iterInorderTraversal = Solution().iterInorderTraversal

def test_inorderTraversal():
    # LeetCode Example 1: root = [1,null,2,3] -> [1,3,2]
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorderTraversal(root) == [1, 3, 2]

    # LeetCode Example 2: root = [1,2,3,4,5,null,8,null,null,6,7,null,9] -> [4,2,6,5,7,1,3,8,9]
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        TreeNode(3, None, TreeNode(8, None, TreeNode(9)))
    )
    assert inorderTraversal(root) == [4, 2, 6, 5, 7, 1, 3, 8, 9]

    # LeetCode Example 3: empty tree
    assert inorderTraversal(None) == []

    # LeetCode Example 4: single node
    assert inorderTraversal(TreeNode(1)) == [1]

    # Edge cases
    # LeetCode Example 1: root = [1,null,2,3] -> [1,3,2]
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert iterInorderTraversal(root) == [1, 3, 2]

    # LeetCode Example 2: root = [1,2,3,4,5,null,8,null,null,6,7,null,9] -> [4,2,6,5,7,1,3,8,9]
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        TreeNode(3, None, TreeNode(8, None, TreeNode(9)))
    )
    assert iterInorderTraversal(root) == [4, 2, 6, 5, 7, 1, 3, 8, 9]

    # LeetCode Example 3: empty tree
    assert iterInorderTraversal(None) == []

    # LeetCode Example 4: single node
    assert iterInorderTraversal(TreeNode(1)) == [1]

    print("All tests passed")

if __name__ == "__main__":
    test_inorderTraversal()
