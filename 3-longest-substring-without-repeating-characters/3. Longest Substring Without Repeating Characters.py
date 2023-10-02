class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cset = set()
        res = 0

        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            res = max(res, r-l+1)

        return res