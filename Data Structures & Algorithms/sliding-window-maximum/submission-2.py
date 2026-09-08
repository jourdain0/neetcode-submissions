class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # stores indices in decreasing order of their values
        l = r = 0

        while r < len(nums):
            # Removes indices whose values are smaller than the new value since they
            # can't be future maximums
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Adding the new index to the deque
            q.append(r)

            # If the left pointer passes the front index, remove it because it's
            # now outside the window
            if l > q[0]:
                q.popleft()
            
            # Once the size of the window is now k, starting adding the front of the
            # deque to res as it is the maximum
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            # Slide the window and repeat
            r += 1
        
        return res