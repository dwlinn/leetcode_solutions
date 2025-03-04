from collections import Counter, defaultdict
from typing import List


class Solution:
    """给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。"""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        left, right, n = 0, 0, len(s)
        result = []
        for right in range(n):
            s_count[s[right]] += 1
            while right - left + 1 == len(p):
                if s_count == p_count:
                    result.append(left)
                if s_count[s[left]] == 1:
                    del s_count[s[left]]
                else:
                    s_count[s[left]] -= 1
                left += 1
        return result

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """从滑动窗口和字符串P的每种字母数量之差来比较"""
        result = []
        counts = [0] * 26  # 记录26个字母分别出现的次数
        left, right, BASE_ORD = 0, 0, 97  # ord("a") = 97
        for letter in p:
            counts[ord(letter) - BASE_ORD] += 1
        for right in range(len(s)):
            counts[(ord(s[right])) - BASE_ORD] -= 1
            while counts[ord(s[right]) - BASE_ORD] < 0:
                counts[ord(s[left]) - BASE_ORD] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
        return result


Solution().findAnagrams("cbaebabacd", "abc")
