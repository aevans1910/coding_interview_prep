#Leetcode code

# Given a sorted array nums, remove the duplicates in-place such that each 
# element appear only once and return the new length. Do not allocate extra 
# space for another array, you must do this by modifying the input array 
# in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums)-1:
            num1 = nums[index]
            num2 = nums[index+1]
            if num1 == num2:
                nums.pop(index)
            else:
                index += 1