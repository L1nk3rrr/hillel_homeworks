#Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down
# to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0


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
    root2.right.right.right = TreeNode(7)

    assert(s.maxDepth(root1) == 3)
    assert(s.maxDepth(root2) == 4)
