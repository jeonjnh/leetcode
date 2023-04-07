class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        ins = 1
        
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[ins] = nums[i]
                ins += 1
                
        return ins
        