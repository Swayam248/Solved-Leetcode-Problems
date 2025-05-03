class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ele=0
        for x in nums:
            c=0
            for y in nums:
                if x==y:
                    c+=1
            if c==1:
                ele = x
                break
        return ele 