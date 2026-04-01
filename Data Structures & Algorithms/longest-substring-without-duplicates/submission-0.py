class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = {}
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] in charset:
                l = max (charset[s[i]]+1, l)
            charset[s[i]] = i
            res = max(res, i - l + 1)
        return res
