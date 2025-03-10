from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
        题目数据保证数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位整数范围内。
        请不要使用除法，且在 O(n) 时间复杂度内完成此题。
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        answer = [prefix[i] * suffix[i] for i in range(n)]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """空间复杂度为O(1)的解法"""
        n = len(nums)
        answer = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
