from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

s = Solution()
print(s.hasDuplicate(nums = [1, 2, 3, 3]))
