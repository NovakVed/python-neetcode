from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums)) != len(nums)):
            return True
        return False

s = Solution()
print(s.hasDuplicate(nums = [1, 2, 3, 3]))
