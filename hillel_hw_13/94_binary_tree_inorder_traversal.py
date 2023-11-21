# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result


if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(6)

    assert (s.inorderTraversal(root1) == [1, 3, 2])
    assert (s.inorderTraversal(root2) == [4, 2, 5, 1, 3, 6])
    assert (s.inorderTraversal([]) == [])
    assert (s.inorderTraversal(TreeNode(1)) == [1])
