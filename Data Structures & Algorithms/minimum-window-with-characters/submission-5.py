class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Use sliding window technique, as well as
        # a hash map to keep track of characters
        # we need and have
        l, r = 0, 0
        res, resLen = [-1, -1], float("infinity")
        sMap, tMap = {}, {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        have, need = 0, len(tMap)

        while r < len(s):
            # Add new character and update have
            # if we have enough of s[r] now
            c = s[r]
            sMap[c] = 1 + sMap.get(c, 0)
            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            # While we have the characters we need
            # shrink the window and update resLen if
            # needed
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                c = s[l]
                sMap[c] -= 1
                l += 1
                if c in tMap and sMap[c] == tMap[c] - 1:
                    have -= 1
            r += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
        