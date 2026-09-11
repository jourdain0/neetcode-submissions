class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            # Include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i]) # Can contain same number unlimitedly
            curr.pop()

            # Skip nums[i]
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res