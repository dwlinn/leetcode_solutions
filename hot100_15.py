from typing import List


class Solution:
    """类比hot100_01:两数之和"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
        同时还满足 nums[i] + nums[j] + nums[k] == 0 。
        请你返回所有和为 0 且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if (curr_sum := nums[left] + nums[right]) == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的 nums[left] 和 nums[right]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return result


print(Solution().threeSum([0, 0, 0, 0]))
