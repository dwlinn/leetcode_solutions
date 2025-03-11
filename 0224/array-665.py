from typing import List


class Solution:
    def IsNotDepressList(self, nums: List[int]) -> bool:
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                return False
        return True

    # def checkPossibility(self, nums: List[int]) -> bool:
    #     for index in range(len(nums) - 1):
    #         x = nums[index]
    #         y = nums[index + 1]
    #         if x > y:
    #             nums[index]  = y
    #             if self.IsNotDepressList(nums):
    #                 return True
    #             nums[index] = x
    #             nums[index + 1] = x
    #             return self.IsNotDepressList(nums)

    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                if i == 0 or (i > 0 and nums[i - 1] <= nums[i + 1]):
                    nums[i] = nums[i + 1]
                    break
                elif nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                    break
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                return False
        return True


print(Solution().checkPossibility([1, 4, 1, 2]))
