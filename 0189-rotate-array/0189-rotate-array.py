class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k > n (like rotating 10 times on an array of size 5)
        nums[:] = nums[-k:] + nums[:-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        