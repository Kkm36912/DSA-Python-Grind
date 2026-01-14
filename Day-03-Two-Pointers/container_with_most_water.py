"""
Day 3: Two Pointers
Problem: Container With Most Water (LeetCode 11)
Difficulty: Medium (Common Interview Question)

My Notes:
- We need to maximize Area = Width * Height.
- Width is determined by the distance between pointers (r - l).
- Height is limited by the SHORTER of the two lines (min(height[l], height[r])).
- Strategy: Greedy Approach. Start with max width (outermost lines).
- To potentially get a larger area, we MUST move the shorter line.
  (Keeping the shorter line limits the height, and width only decreases, so area can't improve).

Time Complexity: O(n) - Single pass.
Space Complexity: O(1) - We only store the max_area variable.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            # Calculate current area
            width = r - l
            h = min(height[l], height[r])
            current_area = width * h
            
            # Update max record
            max_water = max(max_water, current_area)
            
            # Move the pointer of the smaller wall
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                # Optimization: If heights are equal, neither can support a higher water level
                # as width decreases, so we can move both safely.
                l += 1
                r -= 1
                
        return max_water