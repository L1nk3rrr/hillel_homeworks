# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            stack = [root.left, root.right]
            while stack:
                node1, node2 = stack.pop(), stack.pop()
                if node1 is None and node2 is None:
                    continue
                elif node1 is None or node2 is None:
                    return False
                elif node1.val != node2.val:
                    return False
                stack.append(node1.left)
                stack.append(node2.right)
                stack.append(node1.right)
                stack.append(node2.left)
            return True


if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(1)

    root1.left = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)

    root1.right = TreeNode(2)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    root2 = TreeNode(1)

    root2.left = TreeNode(2)
    root2.left.right = TreeNode(3)

    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)

    assert (s.isSymmetric(root1) is True)
    assert (s.isSymmetric(root2) is False)
    assert (s.isSymmetric([]) is None)
    assert (s.isSymmetric(TreeNode(1)) is True)
