class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Make an adjacency list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Use DFS to visit every node in tree. If current node i is
        # in visit, then we have detected a cycle and this is an invalid
        # tree. 
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
        
        # Valid tree: DFS returns true and we have actually
        # visited every node
        return dfs(0, -1) and len(visit) == n