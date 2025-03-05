from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
        子数组是数组中元素的连续非空序列。
        主要思想： sum(i, j) = sum(0, j) - sum(0, i)
        """
        mp = defaultdict(int, {0: 1})  # 统计当前和出现的次数
        pre, count = 0, 0
        for num in nums:
            pre += num
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1
        return count


Solution().subarraySum([1, 1, 1], 2)
