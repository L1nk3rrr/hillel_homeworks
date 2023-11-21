# Given a non-empty array of integers nums, every element appears
# twice except for one.Find that single one.
#
# You must implement a solution
# with a linear runtime complexity and use only constant extra space.
#
# Example 1:
# Input: nums = [2, 2, 1]
# Output: 1
#
# Example2:
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq_num = 0
        for num in nums:
            uniq_num ^= num
        return uniq_num


if __name__ == "__main__":
    s = Solution()
    assert (s.singleNumber([1, 1, 10, 2, 2]) == 10)
    assert (s.singleNumber([1, 1, 2, 3, 2]) == 3)
    assert (s.singleNumber([1, 2, 1, 2]) == 0)
