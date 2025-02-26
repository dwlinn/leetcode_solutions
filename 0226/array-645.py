from typing import List


class Solution:
    """
    集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合丢失了一个数字并且有一个数字重复。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。
    请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
    https://leetcode.cn/problems/set-mismatch/solutions/857255/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """方法1: 哈希表法
        时间复杂度: O(n), 空间复杂度: O(n)
        """
        count = [0] * (len(nums) + 1)
        duplicate, missing = None, None
        for num in nums:
            count[num] += 1
        for i in range(1, len(count)):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i
        return [duplicate, missing]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """方法2：位运算
        优化空间复杂度为O(1)，没太看懂分组异或先不写了
        """
        pass

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """方法3：数学方法
        duplicate = 当前数组元素和 - 去重后的数组元素和
        missing = 数组1~n的和 - 去重后的数组元素和
        """
        n = len(nums)
        curr_sum = sum(nums)
        unique_sum = sum(set(nums))
        origin_sum = n * (n + 1) // 2
        duplicate = curr_sum - unique_sum
        missing = origin_sum - unique_sum
        return [duplicate, missing]


if __name__ == "__main__":
    nums = [2, 2]
    nums = Solution().findErrorNums(nums)
    print(nums)
