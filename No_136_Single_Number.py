"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""
# Runtime 141 ms Beats 61.20%
# Memory 16.7 MB Beats 83.3%

# Bit Operation
# 2 == 0010
# 2 == 0010
# --------- XOR
# 0 == 0000
# 1 == 0001
# --------- XOR
# 1 == 0001

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        res = nums[0]
        for i in range(1,len(nums)):
            res ^= nums[i]

        return res
