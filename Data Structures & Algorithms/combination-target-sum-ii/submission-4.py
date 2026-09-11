class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i]) # Can only include candidates[i] once
            curr.pop()

            # Skip candidates[i], ensuring we skip duplicates too
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res