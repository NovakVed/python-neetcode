from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            anagram_groups[tuple(count)].append(s)

        return list(anagram_groups.values())

s = Solution()
result = s.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)