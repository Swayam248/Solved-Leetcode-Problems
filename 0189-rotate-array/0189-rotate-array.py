class Solution:
    def rotate(self,nums, k):
        # n=len(nums)
        # k=k%n
        # nums[:] = nums[-k:]+nums[:-k]
        nums[:]=nums[-(k%len(nums)):]+nums[:-(k%len(nums))]
        