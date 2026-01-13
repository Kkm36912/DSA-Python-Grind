"""
Day 2: String Manipulation & Hashing
Problem: Group Anagrams (LeetCode 49)
Difficulty: Medium (The Boss Level!)

My Notes:
- Anagrams are words that have the exact same letters (e.g., "eat" and "tea").
- To group them, we need a common "Signature" or "Key".
- Sorting the letters of a word gives us this signature: sorted("tea") -> ['a', 'e', 't'].
- We use a HashMap (Dictionary) where:
    - Key = The sorted tuple of letters (because Lists can't be keys).
    - Value = A list of original words.

Time Complexity: O(N * K log K) - N is number of words, K is length of longest word (sorting takes K log K).
Space Complexity: O(N * K) - To store the map.
"""

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # defaultdict(list) handles the empty list creation automatically
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. Create the signature
            # sorted(word) returns a list ['a', 'e', 't']
            # We MUST convert to tuple ('a', 'e', 't') to use as a dictionary key
            signature = tuple(sorted(word))
            
            # 2. Append original word to that signature's group
            anagram_map[signature].append(word)
            
        # 3. Return the grouped lists (the values of the dictionary)
        return anagram_map.values()