from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            anagrams[key].append(str)
        return list(anagrams.values())


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
