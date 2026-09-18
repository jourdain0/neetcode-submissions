class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r, c))
            q.append([r, c])
        
        # Add all treasure chests to queue and visit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        # Update all rooms with corresponding distances, utilizing the queue
        # to update distance for each round
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addRoom(r + dr, c + dc)
            dist += 1