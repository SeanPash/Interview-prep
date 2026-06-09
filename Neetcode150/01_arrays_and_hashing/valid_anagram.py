# Given two strings s and t, return true if the two strings are anagrams of
# each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another
# string, but the order of the characters can be different.
#
# Example 1:
#   Input: s = "racecar", t = "carrace"
#   Output: true
#
# Example 2:
#   Input: s = "jar", t = "jam"
#   Output: false
#
# Constraints:
#   1 <= s.length, t.length <= 5 * 10^4
#   s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# --- Approach ---
#
# Reading the problem:
# Two strings are anagrams if they use the exact same characters with the same
# frequencies — just in a different order. The brute force would be sorting both
# strings and comparing, which works in O(n log n). But I can do better: the real
# question is "does each character appear the same number of times in both strings?"
# Any time a problem is about counting occurrences and comparing them, that's the
# signal to reach for a hashmap (or frequency array).
#
# How the code works:
# I first short-circuit if the lengths differ — unequal lengths can never be anagrams.
# Then I build two frequency hashmaps in a single pass: countS for s and countT for t.
# For each index i, I increment the count for s[i] in countS and t[i] in countT.
# Finally, I iterate over every character in countS and check that its count matches
# the count in countT (defaulting to 0 if the character is absent). If any count
# differs, the strings are not anagrams.
#
# Time Complexity:
# O(n) — one pass to build both frequency maps, one pass to compare them. Each
# hashmap operation is O(1), so total is linear in the length of the strings.
# Space Complexity: O(1) — the hashmaps hold at most 26 lowercase letter entries,
# which is a fixed upper bound regardless of input size.
