class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for c in range(0, len(s), 1):
            count[ord(s[c]) - ord('a')] += 1
            count[ord(t[c]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
            
        return True

            
            

s = Solution()
print(s.isAnagram(s = "jar", t = "jam"))