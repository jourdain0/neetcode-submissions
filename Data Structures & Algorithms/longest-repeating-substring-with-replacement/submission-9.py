class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxC, res = 0, 0
        count = [0] * 26

        while r < len(s):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            maxC = max(maxC, count[index])
            while (r - l + 1) - maxC > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res