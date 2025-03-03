from typing import List


class Solution:
    """给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    Args:
        height (List[int]): _description_

    Returns:
        int: _description_
    """

    def trap(self, height: List[int]) -> int:
        # 时间复杂度O(n)，空间复杂度O(n)
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0], rightMax[n - 1] = height[0], height[n - 1]
        sum = 0
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for j in range(n - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[j])
        for i in range(0, n):
            sum += min(leftMax[i], rightMax[i]) - height[i]
        return sum

    def trap(self, height: List[int]) -> int:
        # 单调栈
        result, n = 0, len(height)
        stack = [0]
        for i in range(1, n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[top]
                    result += h * (i - stack[-1] - 1)
            stack.append(i)
        return result

   def trap(self, height: List[int]) -> int:
        # 双指针
        result = 0
        left ,right = 0, len(height) - 1
        leftMax = rightMax = 0
        while left < right:
                leftMax, rightMax = max(leftMax, height[left]), max(rightMax, height[right])
                if height[left] < height[right]:
                    result += leftMax - height[left]
                    left += 1
                else:
                    result += rightMax - height[right]
                    right -= 1
        return result
       

Solution().trap([5, 4, 1, 2])
