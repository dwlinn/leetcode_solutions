from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, -1, -1):
            print(i)


Solution().moveZeroes([0,1,0,3,12])
       