# Given a string s consisting of words separated by single spaces, return a new
# string with the order of the words reversed.
#
# A word is defined as a sequence of non-space characters.
#
# Example 1:
#   Input: s = "I love you"
#   Output: "you love I"
#
# Example 2:
#   Input: s = "hello world"
#   Output: "world hello"
#
# Example 3:
#   Input: s = "coding is fun"
#   Output: "fun is coding"
#
# Constraints:
#   1 <= s.length <= 10^4
#   s consists of uppercase and lowercase English letters and single spaces.
#   There are no leading or trailing spaces.
#   Words are separated by exactly one space.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)

# --- Approach ---
#
# Reading the problem:
# I need to reverse the order of words, not characters. The constraints tell me
# words are separated by exactly one space with no leading or trailing spaces,
# so I don't need to handle any edge cases around extra whitespace.
# The core insight is: split the string into a list of words, reverse that list
# in place, then join it back into a string.
#
# How the code works:
# s.split() tokenizes the string by whitespace into a list of words.
# words.reverse() reverses the list in place — no extra copy needed.
# ' '.join(words) reassembles the reversed list into a single space-separated string.
#
# Time Complexity:
# O(n) — split, reverse, and join each touch every character once.
# Space Complexity: O(n) — storing the list of words takes space proportional
# to the length of the input string.
