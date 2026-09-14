"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Similar to other cloning question, keeping track of cloned nodes in a dict
        if not node:
            return None
        oldToNew = {} # original node: cloned node

        def dfs(node):
            # If node is already in oldToNew, we already have a clone, return that
            if node in oldToNew:
                return oldToNew[node]
            
            clone = Node(node.val)
            oldToNew[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)