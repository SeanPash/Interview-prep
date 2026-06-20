# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another
# string, but the order of the characters can be different.
#
# Example 1:
#   Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
#   Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
#
# Example 2:
#   Input: strs = ["x"]
#   Output: [["x"]]
#
# Example 3:
#   Input: strs = [""]
#   Output: [[""]]
#
# Constraints:
#   1 <= strs.length <= 1000
#   0 <= strs[i].length <= 100
#   strs[i] is made up of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

# --- Approach ---
#
# High-level idea:
# Group anagrams by using a frequency count of each word as a signature. Words
# with the same frequency signature are anagrams, so they get grouped together.
#
# How the code works:
# For each word, I build a 26-length array that counts how many times each
# letter appears. I convert that array into a tuple so it can be used as a
# dictionary key — Python lists are mutable and unhashable, but tuples are
# immutable and hashable. I then use a hashmap to bucket every word under its
# signature, and finally return all the grouped values. This works because all
# anagrams produce the exact same frequency signature.
#
# Step by step:
#   1. Create a hashmap: signature -> list of words.
#   2. For each word, build a count array of size 26 and tally each character.
#   3. Convert the count array to a tuple and use it as the key.
#   4. Append the word to that bucket.
#   5. Return all grouped values.
#
# Why not sort each word? Sorting would also produce a shared key, but it costs
# O(k log k) per word. The frequency-count approach is O(k), so it's faster.
#
# Time Complexity:
# O(n * k) — n words, and for each we scan its k characters to build the
# fixed-size 26-length count.
# Space Complexity: O(n * k) — the hashmap stores every word across the buckets.
