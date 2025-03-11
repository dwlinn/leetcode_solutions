from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        need = defaultdict(int)  # 记录t中每个字符出现的次数
        window = defaultdict(int)
        valid = 0
        min_len = float("inf")
        start = 0
        for char in t:
            need[char] += 1  # 初始化need哈希表

        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1

            # 当窗口所有字符都满足need时，尝试缩小窗口
            while valid == len(need):
                # 更新最小窗口
                if right - left < min_len:
                    min_len = right - left
                    start = left

                char_left = s[left]
                left += 1

                if char_left in need:
                    if window[char_left] == need[char_left]:
                        valid -= 1
                    window[char_left] -= 1
        return "" if min_len == float("inf") else s[start : start + min_len]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
