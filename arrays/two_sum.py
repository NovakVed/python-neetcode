from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums), 1):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]] = i

        return []


s = Solution()
print(s.twoSum(nums=[3, 4, 5, 6], target=7))
