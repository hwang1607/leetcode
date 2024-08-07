class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ""

        def check(l, r):
            #check palindrome expanding from l and r

            nonlocal longest
            nonlocal res

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > longest:
                    longest = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
        
        for i in range(len(s)):
            check(i,i)
            check(i, i+1)

        return res