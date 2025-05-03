class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ind =0
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        #     elif nums[i]+1==target:
        #         return i+1
        #     elif target ==0:
        #         return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)