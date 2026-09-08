class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = r = 0
        res = 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, len(window))
            r += 1
        
        return res