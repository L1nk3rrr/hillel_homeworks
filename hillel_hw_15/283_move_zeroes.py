# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array

# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    nums1 = [0]
    nums2 = [0, 1, 0, 3, 0, 5, 0, 12, 0, 1, 4]
    s.moveZeroes(nums)
    s.moveZeroes(nums1)
    s.moveZeroes(nums2)
    assert (nums == [1, 3, 12, 0, 0])
    assert (nums1 == [0, ])
    assert (nums2 == [1, 3, 5, 12, 1, 4, 0, 0, 0, 0, 0])
