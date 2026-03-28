class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(0, len(nums), 1):
            diff = target - nums[i]
            if diff in visited:
                return [visited[diff], i]
            visited[nums[i]] = i

        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
