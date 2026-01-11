"""
Day 1: Arrays & Hashing
Problem: Contains Duplicate (LeetCode 217)
Difficulty: Easy

My Notes:
- The brute force approach (nested loops) would be O(n^2), which is too slow for large inputs.
- We need a way to check for uniqueness instantly.
- Python's `set()` data structure removes duplicates automatically.
- Logic: If the length of the set is different from the length of the original list, duplicates existed.

Time Complexity: O(n) - We iterate through the list once to create the set.
Space Complexity: O(n) - The set stores unique elements.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a set from the list. Sets only store unique elements.
        unique = set(nums)
        
        # If lengths match, no duplicates were removed.
        # If lengths differ, duplicates existed.
        if len(unique) != len(nums):
            return True
        else:
            return False

        # Professional One-Liner version:
        # return len(set(nums)) != len(nums)