class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        maxC, longest = 0, 0
        l, r = 0, 0

        while r < len(s):
            c = ord(s[r]) - ord('A')
            count[c] += 1
            maxC = max(maxC, count[c])

            while (r - l + 1) - maxC > k:
                c = ord(s[l]) - ord('A')
                count[c] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest