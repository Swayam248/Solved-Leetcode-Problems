class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    l.append(i)
                    l.append(j)
                    break
            if len(l) == 2:
                break
        return l