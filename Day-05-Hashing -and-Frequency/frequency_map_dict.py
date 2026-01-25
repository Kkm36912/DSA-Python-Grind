"""Method 1"""
nums = [1,4,4,5,5,6,6,9]
#freq_map = dict()
freq_map = {}
for i in range(1, len(nums)):
  if nums[i] in freq_map:
    freq_map[nums[i]] += 1
  else:
    freq_map[nums[i]]=1
print(freq_map)

"""Time Complexity O(N) and Space Complexity O(N)"""


"""Method 2 in notes"""

