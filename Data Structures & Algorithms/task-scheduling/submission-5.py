class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get the frequencies of each task and append them to a maxHeap
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)
        q = deque() # Queue is used to know when task is next ready to be completed
        time = 0

        while maxHeap or q:
            time += 1

            # If maxHeap is empty, then skip straight to time corresponding to earliest task that can be completed
            if not maxHeap:
                time = q[0][1]
            # For next task in maxHeap, decrease its count and append it to queue if there are still remaining identical tasks
            else:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    q.append([cnt, time + n])
            
            # If we've reached time a task can be completed again, add it to the heap
            if q and time == q[0][1]:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time