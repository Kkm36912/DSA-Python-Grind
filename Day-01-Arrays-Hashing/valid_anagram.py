"""
Day 1: Arrays & Hashing
Problem: Valid Anagram (LeetCode 242)
Difficulty: Easy

My Notes:
- An anagram means two strings have the exact same characters with the exact same frequencies.
- Sorting both strings and comparing them works, but takes O(n log n) time.
- A better approach is using a HashMap (Frequency Map) to count characters.
- Python's `collections.Counter` does this in one line.

Time Complexity: O(n) - We iterate through strings once to count.
Space Complexity: O(1) - Since there are only 26 lowercase English letters, the map size is constant.
"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Counter creates a dictionary of character counts
        # Example: "anagram" -> {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        return Counter(s) == Counter(t)
        #sorted(s) == sorted(t) Another Approach