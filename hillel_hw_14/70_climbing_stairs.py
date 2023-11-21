# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        last, curr = 1,1
        for _ in range(2, n + 1):
            temp = curr
            curr = last + curr
            last = temp
        return curr

if __name__ == "__main__":
    s = Solution()
    assert (s.climbStairs(1) == 1)
    assert (s.climbStairs(2) == 2)
    assert (s.climbStairs(3) == 3)
    assert (s.climbStairs(4) == 5)
