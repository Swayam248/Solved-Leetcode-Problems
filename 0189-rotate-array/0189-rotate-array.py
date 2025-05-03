class Solution:
    def rotate(self,nums, k):
        n=len(nums)
        # k=k%n
        nums[:]=nums[-(k%n):]+nums[:-(k%n)]
        