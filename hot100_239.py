from collections import deque
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
        滑动窗口每次只向右移动一位。返回 滑动窗口中的最大值 。

        分块和预处理方法理解一下
        """
        n = len(nums)
        res = []
        dual_queue = deque()
        for i in range(n):
            while dual_queue and nums[dual_queue[-1]] < nums[i]:  # 保持队列单调递减
                dual_queue.pop()
            dual_queue.append(i)
            while dual_queue[0] <= i - k:
                dual_queue.popleft()
            if i >= k - 1:
                res.append(nums[dual_queue[0]])
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """优先队列"""
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]  # 默认的优先队列是小根堆,所以取个反
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] >= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
