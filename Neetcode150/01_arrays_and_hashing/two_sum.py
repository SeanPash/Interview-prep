# Given an array of integers nums and an integer target, return the indices i and j
# such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that
# satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
#   Input: nums = [3,4,5,6], target = 7
#   Output: [0,1]
#   Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
#   Input: nums = [4,5,6], target = 10
#   Output: [0,2]
#
# Example 3:
#   Input: nums = [5,5], target = 10
#   Output: [0,1]
#
# Constraints:
#   2 <= nums.length <= 1000
#   -10,000,000 <= nums[i] <= 10,000,000
#   -10,000,000 <= target <= 10,000,000
#   Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
        return []

# --- Approach ---
#
# Reading the problem:
# I need to find two numbers in an array that add up to a target and return
# their indices. The brute force would be a nested loop checking every pair —
# that's O(n²). The question I ask myself is: is there a way to avoid that
# inner loop? For each number I look at, I already know exactly what the other
# number needs to be (target - num). So the real question becomes: have I seen
# that number before? Any time a problem is asking "have I seen this before?"
# or "does this value already exist?", that's the signal to reach for a hashmap.
# A hashmap lets me answer that question in O(1) instead of re-scanning the array.
#
# How the code works:
# I create an empty hashmap that maps values to their index.
# I loop through the array with enumerate to get both the index and value.
# For each number, I calculate complement = target - num (the value I need).
# I check if complement is already in the hashmap — if yes, I've found my pair
# and return both indices. If not, I store the current number and its index
# in the hashmap so future iterations can find it.
#
# Time Complexity:
# O(n) — I iterate through the array once. Each lookup and insert into the
# hashmap is O(1), so the total is linear.
# Space Complexity: O(n) — in the worst case I store every element in the hashmap.
