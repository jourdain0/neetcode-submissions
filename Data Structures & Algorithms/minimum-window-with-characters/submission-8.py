class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        hashS, hashT = {}, {}
        res, resLen = [-1, -1], float("infinity")

        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)
        have, need = 0, len(hashT)

        while r < len(s):
            c = s[r]
            hashS[c] = 1 + hashS.get(c, 0)
            if c in hashT and hashS[c] == hashT[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                c = s[l]
                hashS[c] -= 1
                if c in hashT and hashS[c] < hashT[c]:
                    have -= 1
                l += 1
            r += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""