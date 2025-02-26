from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # 递推关系：F(K+1) = F(K) + sum_total - n * nums[n-1-k]
        n = len(nums)
        if n == 1:
            return 0
        sum_total = sum(nums)
        f_curr = sum(i * nums[i] for i in range(n))
        max_val = f_curr
        for k in range(n):
            f_next = f_curr + sum_total - n * nums[n - 1 - k]
            f_curr = f_next
            if max_val < f_next:
                max_val = f_next
        return max_val


if __name__ == "__main__":
    nums = [4, 3, 2, 6]
    count = Solution().maxRotateFunction(nums)
    print(count)
