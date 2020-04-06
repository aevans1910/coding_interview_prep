#Leetcode code, yes the types are defined

#Brute force aproach. Time = On^2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)-1):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

#Hash table solution Time: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  
        for index1 in range(len(nums)):
            needed_num = target - nums[index1]
            if num_dict.get(needed_num) is not None:
                return [index1, num_dict[needed_num]]
            num_dict[nums[index1]] = index1  