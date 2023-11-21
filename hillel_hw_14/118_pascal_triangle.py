# Given an integer numRows, return the first numRows of Pascal's triangle.
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
from typing import List
from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for r in range(numRows):
            row = []
            for k in range(r + 1):
                row.append(
                    int(
                        factorial(r)
                        / (factorial(k)
                           * factorial(r - k)
                           )
                    )
                )
            res.append(row)
        return res


if __name__ == "__main__":
    s = Solution()
    assert (s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    assert (s.generate(1) == [[1]])
    assert (s.generate(0) == [])
