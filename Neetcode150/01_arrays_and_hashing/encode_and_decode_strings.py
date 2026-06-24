# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original
# list of strings.
#
# Machine 1 (sender) has the function:
#   String encode(List<String> strs) { ... return encoded_string; }
# Machine 2 (receiver) has the function:
#   List<String> decode(String encoded_string) { ... return decoded_strs; }
#
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.
#
# Example 1:
#   Input: strs = ["Hello", "World"]
#   Output: ["Hello", "World"]
#
# Example 2:
#   Input: strs = [""]
#   Output: [""]
#
# Constraints:
#   0 <= strs.length < 100
#   0 <= strs[i].length < 200
#   strs[i] contains any possible characters out of 256 valid ASCII characters.
#
# Follow up: Could you write a generalized algorithm to work on any possible
# set of characters?

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            if s[j] != "$":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# --- Approach ---
#
# High-level idea:
# Prefix every string with its length and a delimiter. Storing the length up
# front means decode knows exactly how many characters to read, so the actual
# string contents can hold any character — including the delimiter itself —
# without ambiguity.
#
# How the code works:
# encode walks each string and appends "<length>$<string>" to the result. The
# digits before the "$" tell the decoder how long the upcoming string is, and
# the "$" marks where those digits end.
#
# decode reads the encoded string with a pointer i. From i it advances j past
# the length digits until it hits the "$", parses the integer length, then
# slices out exactly that many characters following the "$". It then jumps i
# past the slice and repeats.
#
# Step by step (decode):
#   1. Start with i at the beginning of the encoded string.
#   2. Advance j to find the "$" that terminates the length prefix.
#   3. Parse s[i:j] as the length of the next string.
#   4. Slice s[j+1 : j+1+length] as the original string and append it.
#   5. Move i to j + 1 + length and repeat until i reaches the end.
#
# Why length-prefixing over a plain separator? A naive separator (like a comma)
# breaks if the data contains that character. Length-prefixing is delimiter-safe
# because we never search the payload for the "$" — we only use it to terminate
# the digits, then read a fixed count of characters. This is the generalized
# answer to the follow up.
#
# Time Complexity: O(n) — encode and decode each touch every character once,
# where n is the total length of all strings.
# Space Complexity: O(n) — the encoded string and the decoded list.
