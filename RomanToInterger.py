#Question: Given a roman numeral, convert it to an integer. Input 
#is guaranteed to be within the range from 1 to 3999.
#Restated question: I need to take a roman numeral from the range of 1 to 3999,
#and turn it into a decimal number interger.

#Questions:
# Will ther always be at least one letter? Will they always be
#capital or will I need to deal with lower case letters? Will
#there be letters I don't have in the dictionary?

#Assumptions:
# For this excercise I will assume that the letters will alwasy be
#capital because that is how roman numerals are written. I will
#also assume that there won't be any letters that aren't in the
#dictionary.

#Time: O(n) This is relativley fast but it does take a bit of space as it uses a 
#dictionary. 

#I need to create the dictionary with the roman numerals in it.
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
        #I need to make sure that it goes through the entire
        #string that is the roman numeral given
        while index1 < len(s) -1:
            val1 = roman[s[index1]]
            val2 = roman[s[index1 +1]]
            
            #If the first value is larger then the second value
            #then I can just add that value as is to a total
            if val1 >= val2:
                total += val1
                index1 += 1
            #If the first value is smaller then the second value,
            #that means that it is grouped in with the numeral after it.
            #I therefore need to substract the first value from the second
            else:
                total += (val2 - val1)
                index1 += 2
                
        #If the last two characters are not substracted, then
        #the while loop will cut off without having taken into
        #account the last value. I therefore need to make sure
        #to catch it and add.
        if index1 < len(s):
            total += roman[s[index1]]
            
        return total