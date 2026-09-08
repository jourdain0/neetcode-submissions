class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Main Solution Idea: Have a dictionary, where the key is
        # the first unique anagram we have encountered and the values
        # are is a list of anagrams that fit with it
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())