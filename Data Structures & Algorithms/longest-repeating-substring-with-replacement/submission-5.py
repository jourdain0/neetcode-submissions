class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = r = 0
        maxC = 0
        res = 0

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxC = max(maxC, freq[s[r]])
            
            while (r - l + 1) - maxC > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res