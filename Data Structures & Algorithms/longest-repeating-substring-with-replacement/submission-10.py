class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = r = 0
        maxC = 0
        res = 0
        
        while r < len(s):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            maxC = max(maxC, count[index])

            while (r - l + 1) - maxC > k:
                index = ord(s[l]) - ord('A')
                count[index] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res