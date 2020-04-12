# Leetcode code

# Write a function to find the longest common prefix string amongst an 
# array of strings. If there is no common prefix, return an empty string "". 
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) <= 1:
            return strs[0]
        
        # strs.sort()
        # print("sorted_strs", strs)
        prefix1 = ""
        prefix2 = ""
        
        i = 2
        # print("strs[-1]:", strs[-1])
        for letter_word_1, letter_word_2, in zip(strs[0], strs[-1]):
            # print ("letter_word_1: ", letter_word_1) 
            # print("letter_word_2: ", letter_word_2)
            if letter_word_1 == letter_word_2:
                prefix1 += letter_word_1
            else:
                break
            
        if len(strs) > 2:
            for letter_word_3, letter_word_2 in zip(prefix1, strs[-i]):
                # print(strs[-i])
                if letter_word_3 == letter_word_2:
                    prefix2 += letter_word_3
                    
                if i < -len(strs)+1:
                    break

        if len(prefix2) > len(prefix1):
            return "".join(prefix2)
        else:
            return "".join(prefix1)