class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k > n (like rotating 10 times on an array of size 5)
        # Because rotating an array of size 7 by 10 steps is the same as rotating it by 10 % 7 = 3 steps.
        nums[:] = nums[-k:] + nums[:-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        