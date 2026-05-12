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
    
    def buildTreeOpt(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        using hashmap to store the root's index in inorder, instead of using inorder.index
            this will get the desired index by O(1) time, no need to traversing list which is O(n)

        define the variable to represent pointer to get current num from preorder,
            each recursion will increment pointer by one,
            and avoid slicing the list to get new list, this will save four lists creating,
            instead, use two pointer left and right to represent the boundary of list

        time = O(n), only traversing preorder
        space = O(n + h), n is for creating hashmap and tree, h is for recursion call
        """
        
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        self.pt = 0
        
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            root = TreeNode(preorder[self.pt])
            self.pt += 1
            
            idx = inorder_idx[root.val]
            root.left = build(left, idx - 1)
            root.right = build(idx + 1, right)
            
            return root
        
        return build(0, len(preorder) - 1)



buildTree = Solution().buildTree
buildTreeOpt = Solution().buildTreeOpt

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
    # LeetCode Example 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] -> [3,9,20,null,null,15,7]
    result = buildTreeOpt([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]

    # LeetCode Example 2: preorder = [-1], inorder = [-1] -> [-1]
    result = buildTreeOpt([-1], [-1])
    assert tree_to_list(result) == [-1]

    print("All tests passed")

if __name__ == "__main__":
    test_buildTree()
