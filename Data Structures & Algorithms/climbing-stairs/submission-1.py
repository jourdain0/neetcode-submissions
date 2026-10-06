class Solution:
    def climbStairs(self, n: int) -> int:
        # Dyanmic Programming, Space optimized Solution
        # one -> ways to reach current step
        # two -> ways to reach previous step
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one