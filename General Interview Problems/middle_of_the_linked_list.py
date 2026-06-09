# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#
# Example 1:
#   Input: head = [1, 2, 3, 4, 5]
#   Output: [3, 4, 5]
#   Explanation: The middle node is node 3.
#
# Example 2:
#   Input: head = [1, 2, 3, 4, 5, 6]
#   Output: [4, 5, 6]
#   Explanation: Two middle nodes exist (3 and 4), return the second one (4).
#
# Constraints:
#   The number of nodes in the list is in the range [1, 100].
#   1 <= Node.val <= 100

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

# --- Approach ---
#
# Reading the problem:
# I need to find the middle of a linked list without knowing its length upfront.
# The naive approach would be to traverse once to count nodes, then traverse again
# to the midpoint — that's two passes. The better question is: can I find the middle
# in a single pass? Yes — using two pointers moving at different speeds.
# If one pointer moves twice as fast as the other, when the fast one reaches the end,
# the slow one will be exactly at the middle.
#
# How the code works:
# Both slow and fast start at head.
# Each iteration, fast moves two steps and slow moves one step.
# The loop runs while fast and fast.next both exist (ensuring fast can safely jump two).
# When fast reaches the end (or has no next), slow is sitting at the middle node.
# For even-length lists, this naturally lands slow on the second middle node.
#
# Time Complexity:
# O(n) — fast traverses the full list, slow traverses half.
# Space Complexity: O(1) — only two pointers regardless of list size.
