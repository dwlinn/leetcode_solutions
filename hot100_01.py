from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
        你可以按任意顺序返回答案。
        """
        dict = {}
        for i in range(len(nums)):
            if (j := target - nums[i]) in dict:
                return [dict[j], i]
            else:
                dict[nums[i]] = i
