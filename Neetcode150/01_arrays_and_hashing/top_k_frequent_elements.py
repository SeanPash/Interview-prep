# Given an integer array nums and an integer k, return the k most frequent
# elements within the array.
#
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
#
# Example 1:
#   Input: nums = [1, 2, 2, 3, 3, 3], k = 2
#   Output: [2, 3]
#
# Example 2:
#   Input: nums = [7, 7], k = 1
#   Output: [7]
#
# Constraints:
#   1 <= nums.length <= 10^4
#   -1000 <= nums[i] <= 1000
#   1 <= k <= number of distinct elements in nums.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# --- Approach ---
#
# High-level idea:
# Use bucket sort on frequency. Instead of sorting elements by how often they
# appear (O(n log n)), I bucket each element by its count and then read buckets
# from the highest count down until I've collected k elements.
#
# How the code works:
# First I build a hashmap of element -> count. Then I create a list of buckets
# indexed by frequency, where freq[c] holds every element that appears exactly
# c times. Since an element can appear at most len(nums) times, len(nums) + 1
# buckets cover every possible frequency. Finally I walk the buckets from the
# highest index downward, collecting elements until res has k of them.
#
# Step by step:
#   1. Tally each element's count in a hashmap.
#   2. Create freq buckets: freq[c] = list of elements seen exactly c times.
#   3. Place each element into the bucket matching its count.
#   4. Iterate buckets from highest frequency to lowest.
#   5. Append elements to res and return once len(res) == k.
#
# Why bucket sort over a heap? A heap-based answer is O(n log k). Bucket sort is
# O(n) because frequencies are bounded by the array length, so we avoid the log
# factor entirely.
#
# Time Complexity: O(n) — one pass to count, one pass to bucket, and the bucket
# scan touches each element at most once.
# Space Complexity: O(n) — the count map and the frequency buckets.
