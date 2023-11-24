# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)  # append an opening tag
            elif not stack or bracket != pairs[stack.pop()]:  # check for closing bracket
                return False

        # check if stack contains unmatched bracket
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()

    assert (s.isValid('()') == True)
    assert (s.isValid('()[]{}') == True)
    assert (s.isValid('(]') == False)
    assert (s.isValid('({})') == True)
