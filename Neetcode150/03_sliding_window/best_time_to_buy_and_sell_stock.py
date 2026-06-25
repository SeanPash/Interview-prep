# You are given an integer array prices where prices[i] is the price of
# NeetCoin on the ith day.
#
# You may choose a single day to buy one NeetCoin and choose a different day in
# the future to sell it.
#
# Return the maximum profit you can achieve. You may choose to not make any
# transactions, in which case the profit would be 0.
#
# Example 1:
#   Input: prices = [10,1,5,6,7,1]
#   Output: 6
#   Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
#
# Example 2:
#   Input: prices = [10,8,7,5,2]
#   Output: 0
#   Explanation: No profitable transactions can be made, thus the max profit is 0.
#
# Constraints:
#   1 <= prices.length <= 100
#   0 <= prices[i] <= 100

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

# --- Approach ---
#
# High-level idea:
# Use two pointers as a sliding window where l marks the buy day (the cheapest
# price seen so far) and r scans forward as the sell day. The profit for any
# window is prices[r] - prices[l], and we track the best one seen.
#
# How the code works:
# l starts at the buy candidate and r scans every day. If prices[r] is higher
# than prices[l], selling on day r is profitable, so we compute that profit and
# update maxProfit. If prices[r] is not higher, then day r is a cheaper (or
# equal) buy point, so we slide l up to r — there is never a reason to buy at a
# higher price than one available later.
#
# Step by step:
#   1. Place both pointers at day 0 and set maxProfit to 0.
#   2. For each r, if prices[r] > prices[l], record profit = prices[r] - prices[l]
#      and keep the maximum.
#   3. Otherwise move l to r, since r is the new cheapest buy candidate.
#   4. Advance r and repeat until the array is exhausted.
#
# Why moving l to a lower price works: a future sell can only benefit from the
# lowest preceding buy price, so whenever we find a new minimum we anchor the
# window there. This guarantees we always measure profit against the best
# possible buy day so far.
#
# Time Complexity: O(n) — a single pass over prices.
# Space Complexity: O(1) — only a few pointers and counters.
