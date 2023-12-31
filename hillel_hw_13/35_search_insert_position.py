# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end + 1

if __name__ == "__main__":
    s = Solution()
    assert (s.searchInsert([1, 3, 5, 6], 5) == 2)
    assert (s.searchInsert([1, 3, 5, 6], 2) == 1)
    assert (s.searchInsert([1, 3, 5, 6], 4) == 2)
    assert (s.searchInsert([1, 3, 5, 6], 7) == 4)
