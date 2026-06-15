# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false.
#
# Example 1:
#   Input: nums = [1, 2, 3, 3]
#   Output: true
#
# Example 2:
#   Input: nums = [1, 2, 3, 4]
#   Output: false
#
# Constraints:
#   0 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

# --- Approach ---
#
# Reading the problem:
# The question is simply "have I seen this value before?" Any time a problem asks
# about detecting repeats, that's the signal to reach for a hashset, which gives
# O(1) average membership checks. The brute force would compare every pair in
# O(n^2), and sorting first would be O(n log n); a set beats both at O(n).
#
# How the code works:
# I keep a set of values I've already seen. For each number, I check if it's
# already in the set — if so, I've found a duplicate and return True immediately.
# Otherwise I add it to the set and continue. If the loop finishes without an early
# return, every value was unique, so I return False.
#
# Time Complexity:
# O(n) — a single pass over nums with O(1) average set lookups and inserts.
# Space Complexity: O(n) — in the worst case (all unique) the set holds every value.
