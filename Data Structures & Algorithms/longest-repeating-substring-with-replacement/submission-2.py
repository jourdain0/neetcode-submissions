class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r  = 0, 0
        count = [0] * 26
        maxC = 0
        res = 0
        
        while r < len(s):
            count[(ord(s[r]) - ord('A'))] += 1
            maxC = max(maxC, count[ord(s[r]) - ord('A')])
            while (r - l + 1) - maxC > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res