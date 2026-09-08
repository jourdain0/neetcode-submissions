class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        sMap, tMap = {}, {}
        res, resLen = [-1, -1], float("infinity")

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        have, need = 0, len(tMap)

        while r < len(s):
            c = s[r]
            sMap[c] = 1 + sMap.get(c, 0)
            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                c = s[l]
                sMap[c] -= 1
                if c in tMap and sMap[c] < tMap[c]:
                    have -= 1
                l += 1
            r += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""