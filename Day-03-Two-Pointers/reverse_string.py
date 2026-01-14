"""
Day 3: Two Pointers
Problem: Reverse String (LeetCode 344)
Difficulty: Easy

My Notes:
- The problem requires modifying the string (list of characters) IN-PLACE.
- We cannot allocate a new array (Space must be O(1)).
- Logic: Use two pointers. One at the start (l), one at the end (r).
- Swap the characters at l and r, then move them towards the center.
- Stop when l >= r.

Time Complexity: O(n) - We touch every character once.
Space Complexity: O(1) - No extra memory used.
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            # Pythonic swap - no temp variable needed
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1