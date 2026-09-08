class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print("x: " + str(x))
            print("y: " + str(y))
            print()
            if x == y:
                continue
            else:
                heapq.heappush_max(stones, x - y)
        
        return stones[0] if len(stones) == 1 else 0