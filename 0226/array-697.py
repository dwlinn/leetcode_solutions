from typing import List


class Solution:
    """
    给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
    """

    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        先确定度，再确定度最大元素所在的位置（可能有多个元素出现频率相同），再比较这些元素所确定的连续子数组长度
        """
        nums_dict = dict()
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [1, i, i]  # 出现次数，第一次出现位置，最后一次出现位置
            else:
                nums_dict[num][0] += 1  # 更新出现次数
                nums_dict[num][2] = i  # 更新最后一次出现位置

        degree, minLen = 0, 0
        for cnt, i, j in nums_dict.values():
            if degree < cnt:
                degree = cnt
                minLen = j - i + 1
            elif degree == cnt and j - i + 1 < minLen:
                minLen = j - i + 1
        return minLen


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1]
    Solution().findShortestSubArray(nums)
