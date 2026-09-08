class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify_max(maxHeap)

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush_max(maxHeap, [dist, x, y])

        while len(maxHeap) > k:
            heapq.heappop_max(maxHeap)
        
        res = []
        while maxHeap:
            _, x, y = heapq.heappop_max(maxHeap)
            res.append([x, y])
        
        return res