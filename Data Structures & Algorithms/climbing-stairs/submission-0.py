class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = {1: 1, 2: 2}
        steps = 3

        while steps != n:
            ways[steps] = ways[steps - 2] + ways[steps - 1]
            steps += 1
        
        return ways[steps - 2] + ways[steps - 1]