class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j: #i!=j as we cannot add same element(case 2 - 3+3 is not allowed)
                    l.append(i)
                    l.append(j)
                    break
            if len(l) == 2:  #already 2 elements in list? solved. break
                break
        return l