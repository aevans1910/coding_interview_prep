#Leetcode code, yes the types are defined

#Question: Given an array of integers, return indices of the two 
#numbers such that they add up to a specific target.

#How do I return the indices? Do I return them as an array? How big can
#this array be? Will there always be a solution? Will there only be one
#solution? May I use the same element twice?

#(Some assumptions come from Leetcode) I assume that each input will always
#have exactly one solution. I will also assume that I may not use the same
#element twice. I will also assume that I will return the indices as an
#array.

#Brute force aproach. Time = On^2
#This is not the way to do it
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)-1):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

#Hash table solution Time: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Need to create a dictionary to store all the relations
        #between the index and the element at that index
        num_dict = {}  
        #Need to loop through the elements in the array
        for index1 in range(len(nums)):
            #We will subtract the number at that index from the
            #target to get the number we need (number that if 
            # added to current index's number will have a sum of
            # the target)
            needed_num = target - nums[index1]
            #If the number we need is already in the dictionary
            if num_dict.get(needed_num) is not None:
                #Return the indexes of the solution
                return [index1, num_dict[needed_num]]
            #Else add the number of the index to the dictionary
            num_dict[nums[index1]] = index1  