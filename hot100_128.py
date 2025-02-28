from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums_set)
        if n < 2:
            return n
        longest_streak = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    count += 1
                    curr_num += 1
                if longest_streak < count:
                    longest_streak = count
        return longest_streak


print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
