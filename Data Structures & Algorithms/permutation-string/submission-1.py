class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        count2 = [0] * 26
        for i in range(0, len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if count1 == count2:
                return True
            r += 1
            if r == len(s2):
                break
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            count2[ord(s2[r]) - ord('a')] += 1
        
        return False
