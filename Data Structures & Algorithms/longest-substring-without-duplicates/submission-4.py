class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Can use a hash set and sliding window to
        # find the longest substring as we traverse
        # the string
        window = set()
        l = r = longest = 0

        while r < len(s):
            # Remove chars left of window until
            # new character will be unique
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            # Add new character
            window.add(s[r])

            # Update longest if needed and move to
            # next character
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
