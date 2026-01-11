"""
Day 1: Arrays & Hashing
Problem: Two Sum (LeetCode 1)
Difficulty: Easy (The most famous interview question!)

My Notes:
- Brute Force (Nested Loops) checks every pair, taking O(n^2). This causes Time Limit Exceeded.
- Optimization: Use a HashMap (Dictionary) to act as a "Memory Diary".
- As we iterate, we calculate: 'needed_value = target - current_value'.
- If 'needed_value' is already in our map, we found the pair!
- If not, we store the current number and its index in the map for future checks.

Time Complexity: O(n) - One pass through the array.
Space Complexity: O(n) - To store the visited numbers in the map.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store { Value : Index }
        # This helps us look up if we have seen a number before in O(1) time.
        seen = {}
        
        for i, n in enumerate(nums):
            # Calculate what number we need to reach the target
            diff = target - n
            
            # Check if that needed number is already in our 'Memory Diary'
            if diff in seen:
                # If yes, return the index of the old number and the current index
                return [seen[diff], i]
            
            # If no, add the current number to the map
            seen[n] = i
            
        return [] # Return empty if no solution found