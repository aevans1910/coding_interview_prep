#Leetcode code, yes the types are defined

#Brute force aproach. Time = On^2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)-1):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]