# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward. It is also
# case-insensitive and ignores all non-alphanumeric characters.
#
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
#
# Example 1:
#   Input: s = "Was it a car or a cat I saw?"
#   Output: true
#   Explanation: After considering only alphanumerical characters we have
#   "wasitacaroracatisaw", which is a palindrome.
#
# Example 2:
#   Input: s = "tab a cat"
#   Output: false
#   Explanation: "tabacat" is not a palindrome.
#
# Constraints:
#   1 <= s.length <= 1000
#   s is made up of only printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

# --- Approach ---
#
# Reading the problem:
# I need to check if a string is the same forwards and backwards, ignoring
# case and non-alphanumeric characters. The key insight from the definition
# of a palindrome is that it's symmetric — the first character mirrors the last,
# the second mirrors the second-to-last, and so on. Whenever a problem has that
# kind of mirror/symmetric structure where I need to compare opposite ends of a
# sequence, two pointers is the natural fit. One pointer starts at the left,
# one at the right, and I move them toward each other. This avoids creating a
# cleaned copy of the string and lets me check in a single pass with O(1) space.
#
# How the code works:
# I initialize l at index 0 and r at the last index.
# Before comparing, I advance l forward and r backward past any non-alphanumeric
# characters using isalnum() — this handles spaces, punctuation, etc.
# Then I compare s[l].lower() and s[r].lower() to make it case-insensitive.
# If they don't match I immediately return False.
# If they do match, I move both pointers one step inward and repeat.
# If the pointers meet or cross without finding a mismatch, the string is a
# palindrome and I return True.
#
# Time Complexity:
# O(n) — each character is visited at most once as l and r move toward each other.
# Space Complexity: O(1) — only two integer pointers, no extra data structures.
