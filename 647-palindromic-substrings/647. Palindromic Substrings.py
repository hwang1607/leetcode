class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def check(l,r):
            nonlocal ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans+= 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            check(i,i)
            check(i, i+1)
        
        return ans

        