# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(0,len(nums)):
            try:
                if target-nums[i] in nums:
                    print(target-nums[i])
                    print(nums.index(target-nums[i],i+1,len(nums)))
                    return i,nums.index(target-nums[i],i+1,len(nums))
            except:
                pass
