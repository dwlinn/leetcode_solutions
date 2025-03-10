from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """_summary_
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。
        说明：你不能倾斜容器。
        """
        i, j = 0, len(height) - 1
        maxArea = 0
        while i < j:
            x = j - i
            y = min(height[i], height[j])
            if (area := x * y) > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
