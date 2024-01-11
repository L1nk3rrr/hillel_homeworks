# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.left = TreeNode(3)

    assert(s.isSameTree(root1, root2) is False)
    assert(s.isSameTree(root1, root3) is True)
