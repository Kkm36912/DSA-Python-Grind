"""
Day 2: String Manipulation
Problem: Longest Common Prefix (LeetCode 14)
Difficulty: Easy

My Notes:
- We need to find the starting string pattern shared by ALL strings in the list.
- Brute force (checking every string against every other) is unnecessary.
- SMART TRICK: Sort the list of strings alphabetically.
- After sorting, the "most different" strings will be at the very start (Index 0) and very end (Index -1).
- If the First and Last strings share a prefix, then ALL strings in between must also share it.

Time Complexity: O(N log N) - Because sorting takes the most time.
Space Complexity: O(1) - We only store the result string.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Sort the list alphabetically
        # Example: ["flower", "flow", "flight"] -> ["flight", "flow", "flower"]
        strs.sort()
        
        # Compare only the first and last string
        first = strs[0]
        last = strs[-1]
        
        ans = ""
        
        # Loop through the length of the shorter string
        for i in range(min(len(first), len(last))):
            # If characters match, add to answer
            if first[i] == last[i]:
                ans += first[i]
            else:
                # If mismatch found, stop immediately
                return ans
                
        return ans