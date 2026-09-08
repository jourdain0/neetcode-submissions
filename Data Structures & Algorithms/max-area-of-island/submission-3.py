class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # My DFS solution, but seems to be a lot slower than others
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] != 1):
                return 0
            
            visit.add((r, c))
            return 1 + (dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c):
                    res = max(res, dfs(r, c))
        
        return res