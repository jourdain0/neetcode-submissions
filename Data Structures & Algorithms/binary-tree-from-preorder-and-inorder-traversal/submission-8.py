# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx

            # Whole tree has been constructed
            if preIdx >= len(preorder):
                return None
            
            # Part of tree has been constructed, move on to next
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            # Make new node, increment preIdx, and construct left and right branches
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))