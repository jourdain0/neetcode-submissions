class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS Solution
        # Create adjacency list
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Use DFS to visit all connected neighbors
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        # Increment res each time we visit a new component (found a node we
        # haven't visited after already running dfs)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res