class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Case: If len(s1) is longer than len(s2) then
        # it's impossible for s2 to contain a permutation
        # of s1
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        l, r = 0, 0

        # Set s1Count and and set window at beginning of s2
        while r < len(s1):
            s1Count[ord(s1[r]) - ord('a')] += 1
            s2Count[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        # Check for current matches if s2Count == s1Count
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        # Slide window until permutation has been found, else
        # return false
        while r < len(s2):
            if matches == 26:
                return True
            
            # Remove left char, check for changes in matches
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            l += 1
            
            # Add right char, check for changes in matches
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            r += 1
        
        return matches == 26