from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        是数组中的一个连续部分。
        """
        # 动态规划
        # current_max = max(current_max + nums[i], nums[i])
        # global_max = max(global_max, current_max)
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            global_max = max(global_max, current_max)
        return global_max

    def maxSubArray(self, nums: List[int]) -> int:
        # 分治法
        def divide_and_conquer(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # 递归求解左半部分和右半部分
            left_max = divide_and_conquer(left, mid)
            right_max = divide_and_conquer(mid + 1, right)

            # 计算跨越中间的最大子数组和
            # 左半部分
            left_sum = float("-inf")
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)

            # 右半部分
            right_sum = float("-inf")
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)

            # 跨越中间的最大子数组和
            cross_max = left_sum + right_sum

            # 合并结果
            return max(left_max, right_max, cross_max)

        return divide_and_conquer(0, len(nums) - 1)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
