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

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """还没有想特别清楚

        Args:
            s (str): _description_
            p (str): _description_

        Returns:
            List[int]: _description_
        """
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)
        for i in range(s_len - p_len):
            if (
                count[ord(s[i]) - 97] == 1
            ):  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif (
                count[ord(s[i]) - 97] == 0
            ):  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if (
                count[ord(s[i + p_len]) - 97] == -1
            ):  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif (
                count[ord(s[i + p_len]) - 97] == 0
            ):  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans


Solution().findAnagrams("cbaebabacd", "abc")
