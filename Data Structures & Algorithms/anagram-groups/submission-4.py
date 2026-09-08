class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Have a dictionary that stores unique count arrays that
        # serve as the keys for anagrams that match the array
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())
