from typing import List


class Solution:
    """
    集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合丢失了一个数字并且有一个数字重复。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。
    请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
    https://leetcode.cn/problems/set-mismatch/solutions/857255/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        方法1: 哈希表法
        时间复杂度: O(n), 其中 n 是数组的长度。需要遍历两次数组, 每次遍历的时间复杂度是 O(n)。
        空间复杂度: O(n), 其中 n 是数组的长度。需要创建一个长度为 n+1 的数组。
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


if __name__ == "__main__":
    nums = [1, 1]
    nums = Solution().findErrorNums(nums)
    print(nums)
