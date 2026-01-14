"""
Day 3: Two Pointers
Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)
Difficulty: Medium

My Notes:
- Unlike the standard Two Sum, the array here is SORTED.
- This allows us to use Two Pointers instead of a HashMap.
- If the current sum is TOO BIG, we need a smaller number -> Move Right pointer left.
- If the current sum is TOO SMALL, we need a bigger number -> Move Left pointer right.
- This optimization brings Space Complexity down to O(1) compared to O(n) for HashMap.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                # Problem asks for 1-based index
                return [l + 1, r + 1]