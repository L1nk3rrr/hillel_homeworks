#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

from typing import List


class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        days_count = len(temperatures)

        next_warm_day = [0 for _ in range(days_count)]

        for day in range(days_count - 2, -1, -1):
            next_day = 1

            # iterate like node structure
            while next_day and temperatures[day + next_day] <= temperatures[day]:
                if next_warm_day[day + next_day]:
                    next_day += next_warm_day[day + next_day]
                else:
                    next_day = 0
            next_warm_day[day] = next_day

        return next_warm_day

if __name__ == "__main__":
    s = Solution()
    assert (s.daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    assert (s.daily_temperatures([30,40,50,60]) == [1,1,1,0])
    assert (s.daily_temperatures([30,60,90]) == [1,1,0])
