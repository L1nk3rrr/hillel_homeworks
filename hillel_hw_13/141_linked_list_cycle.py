# Definition for singly-linked list.\
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
# is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We will use fast and slow pointers

        # So if head or head.next is None -> we don't have a cycle
        if head == None or head.next == None:
            return False

        fast = head
        slow = head
        # go through the loop while next and next.next will not equal to None
        while (fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    root1 = ListNode(1)

    root1.next = ListNode(2)
    root1.next.next = ListNode(0)
    root1.next.next.next = ListNode(4)
    root1.next.next.next.next = root1.next

    root2 = ListNode(1)

    root2.next = ListNode(2)
    root2.next.next = ListNode(0)
    root2.next.next.next = ListNode(4)

    assert (s.hasCycle(root1) is True)
    assert (s.hasCycle(root2) is False)
