class Solution:
    """给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result = 0, 0, 0
        n = len(s)
        substr_set = set()
        for right in range(n):
            while left <= right and s[right] in substr_set:
                substr_set.remove(s[left])
                left += 1
            substr_set.add(s[right])
            result = max(result, right - left + 1)
        return result
