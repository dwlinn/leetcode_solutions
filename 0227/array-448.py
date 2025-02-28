from typing import List


class Solution:
    """
    给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
    """

    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     count = [0] * (len(nums) + 1)
    #     for num in nums:
    #         count[num] += 1
    #     return [i for i in range(1, len(count)) if count[i] == 0]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 改进空间复杂度为O(1),将元素值作为下标，将下标对应的元素值变为负数，最后遍历数组，元素值为正数的下标即为缺失的数字
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:  # 如果当前下标元素未被标记
                nums[idx] = -nums[idx]
        return [i for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
