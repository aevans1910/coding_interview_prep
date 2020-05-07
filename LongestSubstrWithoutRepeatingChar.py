# Leetcode code

# Given a string, find the length of the longest substring without 
# repeating characters.

# Time complexity: O(n) for going through n characters in the string
# Space complexity: O(n) for creating a dictionary with n items in it

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Need to go through all of the characters
        # Need to keep track of index at which substring starts
        # When a repeating letter appears, the sub string stops
        # Need to compare substrings to find the longest one
        
        used = {} # O(n) space complexity for a dictionary with n items in it
        max_len = start = 0 # O(1) space complexity for creating varaible
        
        for index, char in enumerate(s): # O(n) time complexity for going through
            #all the characters in the given string
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, index - start + 1)
            
            used[char] = index
        
        return max_len