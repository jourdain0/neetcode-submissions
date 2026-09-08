class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freqs = {}

        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)
        
        for num, cnt in freqs.items():
            buckets[cnt].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res