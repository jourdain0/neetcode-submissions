class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Can use hash map and sliding window, using the
        # hash map to keep track of frequencies and a size
        # changing sliding window to track longest window
        # you can have and still be valid. Also keep track
        # of character with highest frequency to help
        # make sure it's valid for most k replacements
        count = [0] * 26
        l, r, maxC, longest = 0, 0, 0, 0

        while r < len(s):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            maxC = max(maxC, count[index])

            # Make window valid before checking if this
            # is the longest window
            while (r - l + 1) - maxC > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest