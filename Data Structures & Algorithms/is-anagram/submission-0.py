class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict1 = {}
        myDict2 = {}
        for i in range(len(s)):
            myDict1[s[i]] = myDict1.get(s[i]) + 1 if s[i] in myDict1 else 1
            myDict2[t[i]] = myDict2.get(t[i]) + 1 if t[i] in myDict2 else 1
        return myDict1 == myDict2