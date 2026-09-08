class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r = 0, 0
        longest = 0
        length = 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                length -= 1
                l += 1
            window.add(s[r])
            length += 1
            longest = max(longest, length)
            r += 1
        
        return longest