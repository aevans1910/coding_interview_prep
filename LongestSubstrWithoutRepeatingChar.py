# Leetcode code

# Given a string, find the length of the longest substring without 
# repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Need to go through all of the characters
        # Need to keep track of index at which substring starts
        # When a repeating letter appears, the sub string stops
        # Need to compare substrings to find the longest one
        
        used = {}
        max_len = start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, index - start + 1)
            
            used[char] = index
        
        return max_len