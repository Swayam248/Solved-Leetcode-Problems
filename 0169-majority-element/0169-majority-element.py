class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         # ele=0
#         # for x in nums:
#         #     c=0
#         #     for y in nums:
#         #         if x==y:
#         #             c+=1
#         #     if c>(len(nums)/2):
#         #         ele=x
#         #         break
#         # return ele
#         for x in nums:
#             count = 0
#             for y in nums:
#                 if x == y:
#                     count += 1
#             if count > len(nums) // 2:
#                 return x
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
