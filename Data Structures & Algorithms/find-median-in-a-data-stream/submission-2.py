class MedianFinder:

    def __init__(self):
        # two heaps, large, small, min heap, max heap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)

        # make sure every num in small is <= every num in large
        if (self.small and self.large and self.small[0] > self.large[0]):
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        
        # make sure sizes are even
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)
          

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.small[0] + self.large[0]) / 2
        