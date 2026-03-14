class Solution:
    def isPalindrome(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            left = i
            right = len(s) - i - 1
            if s[left] != t[right]:
                return False
        return True

s = Solution()
print(s.isPalindrome("anagram", "nagaram"))