#Time: O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        index1 = 0
        while index1 < len(s) -1:
            val1 = roman[s[index1]]
            val2 = roman[s[index1 +1]]
            
            if val1 >= val2:
                total += val1
                index1 += 1
            else:
                total += (val2 - val1)
                index1 += 2
                
        if index1 < len(s):
            total += roman[s[index1]]
            
        return total