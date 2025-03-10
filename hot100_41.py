from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
        请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
        """
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


Solution().firstMissingPositive([3, 4, -1, 1])
