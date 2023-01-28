"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for num in nums:
            if(num != 0):
                temp.append(num)

        for i in range(len(nums)):
            if(i<len(temp)):
                nums[i] = temp[i]
            else:
                nums[i] = 0
