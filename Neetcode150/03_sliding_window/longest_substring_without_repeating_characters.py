# Given a string s, find the length of the longest substring without duplicate
# characters.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#   Input: s = "zxyzxyz"
#   Output: 3
#   Explanation: The string "xyz" is the longest without duplicate characters.
#
# Example 2:
#   Input: s = "xxxx"
#   Output: 1
#
# Constraints:
#   0 <= s.length <= 1000
#   s may consist of printable ASCII characters.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l = 0, 0
        counter = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest

# --- Approach ---
#
# Reading the problem:
# I need the longest contiguous window of characters where no character repeats.
# The brute force checks every substring — O(n²) or worse. The better question
# is: can I maintain a valid window and just slide it? Yes — this is a variable-
# size sliding window. I expand the right edge freely, and only shrink the left
# edge when a duplicate enters the window. Because each character is added and
# removed at most once, the total work stays O(n).
#
# How the code works:
# I keep a frequency map (counter) of characters in the current window [l, r].
# For each new character at r, I increment its count.
# If that character's count exceeds 1, there's a duplicate — I shrink from the
# left by decrementing counter[s[l]] and advancing l, until the duplicate is gone.
# After the while loop the window is valid again, so I update longest with its size
# (r - l + 1).
#
# Time Complexity:
# O(n) — r advances n times and l advances at most n times total across all iterations.
# Space Complexity: O(1) — the counter holds at most 128 ASCII characters, a fixed bound.
