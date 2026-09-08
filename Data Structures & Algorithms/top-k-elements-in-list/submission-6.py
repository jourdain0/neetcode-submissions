class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        