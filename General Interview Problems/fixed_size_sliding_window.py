# Given an array (list) nums consisted of only non-negative integers, find the
# largest sum among all subarrays of length k in nums.
#
# Example:
#   Input: nums = [1, 2, 3, 7, 4, 1], k = 3
#   Output: 14
#   Explanation: The largest length-3 subarray sum is [3, 7, 4] which sums to 14.

def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)
    return largest

# --- Approach ---
#
# Reading the problem:
# I need the maximum sum of any contiguous subarray of exactly length k.
# The brute force would be a nested loop recalculating the sum of every k-length
# subarray from scratch — that's O(n * k). The key observation is that as the
# window slides one position to the right, only two elements change: I lose the
# leftmost element and gain a new rightmost element. Everything in between stays
# the same. That "slide by adding one and removing one" pattern is the sliding
# window technique, and it brings the cost per slide down to O(1).
#
# How the code works:
# First, I compute the sum of the initial window (the first k elements).
# I set largest to that sum as the starting best.
# Then I slide the window from index k to the end of the array.
# For each new position of right, left = right - k is the element falling out.
# I subtract nums[left] and add nums[right] to update window_sum in O(1).
# I update largest if the new window_sum exceeds it.
#
# Time Complexity:
# O(n) — one pass to build the initial window, one pass to slide it.
# Space Complexity: O(1) — only a few variables regardless of input size.
