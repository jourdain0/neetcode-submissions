class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freqs = {}
        maxC = 0
        res = 0

        while r < len(s):
            # Add new character to window
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxC = max(maxC, freqs[s[r]])

            # Shrink window until window is valid
            while (r - l + 1 - maxC > k):
                freqs[s[l]] -= 1
                l += 1
            
            # Update res if needed and go to next position
            res = max(res, r - l + 1)
            r += 1
        
        return res