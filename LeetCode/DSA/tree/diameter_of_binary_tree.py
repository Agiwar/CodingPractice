class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:    
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        there must be one node, calculate root's max depth of left and right subtree, respectively
            and use DFS to recursive this execution,
            cuz the expected answer does not always happen on the root,
            the longest path between two nodes may be in subtree,
            and need to visit each node to calculate their height and diameter,
            per-node works O(1) time, so total time is O(n),
            and space complexity is typically O(h), O(n) in worse case if skewed tree

        time = O(n)
        space = O(h) typically, worst O(n)
        """
        
        def get_height_diameter(curr: TreeNode | None) -> tuple[int, int]:
            if not curr:
                return (0, 0)
            
            left_height, left_diameter = get_height_diameter(curr.left)
            right_height, right_diameter = get_height_diameter(curr.right)
            
            height = max(left_height, right_height) + 1
            diameter = max(left_diameter, right_diameter, left_height + right_height)
            
            return (height, diameter)
        
        _, diameter = get_height_diameter(root)
        return diameter


diameterOfBinaryTree = Solution().diameterOfBinaryTree


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


def test_diameterOfBinaryTree():
    # LeetCode examples
    assert diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
    assert diameterOfBinaryTree(build_tree([1, 2])) == 1

    # Edge cases
    assert diameterOfBinaryTree(build_tree([1])) == 0

    print("All tests passed")


if __name__ == "__main__":
    test_diameterOfBinaryTree()
