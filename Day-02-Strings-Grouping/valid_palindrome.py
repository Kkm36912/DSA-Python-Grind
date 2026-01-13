"""
Day 2: String Manipulation
Problem: Valid Palindrome (LeetCode 125)
Difficulty: Easy

My Notes:
- A palindrome reads the same forwards and backwards.
- We need to ignore spaces, punctuation, and case sensitivity.
- Python String Method `isalnum()` is useful to filter only letters and numbers.
- Slicing `[::-1]` is the fastest way to reverse a list or string in Python.

Time Complexity: O(n) - We iterate through the string once to clean it, then once to compare.
Space Complexity: O(n) - We create a new list for the cleaned characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # List Comprehension Step:
        # 1. Loop through each char in 's'
        # 2. Keep it ONLY if it is alphanumeric (a-z, 0-9)
        # 3. Convert it to lowercase
        new_s = [char.lower() for char in s if char.isalnum()]
        
        # Check if the list matches its reverse
        return new_s == new_s[::-1]