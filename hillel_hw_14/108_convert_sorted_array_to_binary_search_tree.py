# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# Example 1:
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # top of tree/node view
        middle_node = len(nums) // 2

        return TreeNode(
            nums[middle_node],
            # left side
            self.sortedArrayToBST(nums[:middle_node]),
            # right side
            self.sortedArrayToBST(nums[middle_node + 1:])
        )


def identical_trees(x_tree: TreeNode, y_tree: TreeNode):
    if x_tree is None and y_tree is None:
        return True

    if x_tree is not None and y_tree is not None:
        return (
                (x_tree.val == y_tree.val)
                and identical_trees(x_tree.left, y_tree.left)
                and identical_trees(x_tree.right, y_tree.right)
        )
    return False


if __name__ == "__main__":
    s = Solution()

    ans = TreeNode(0)
    ans.left = TreeNode(-3)
    ans.right = TreeNode(9)
    ans.left.left = TreeNode(-10)
    ans.right.left = TreeNode(5)

    assert (identical_trees(s.sortedArrayToBST([-10, -3, 0, 5, 9]), ans) is True)
