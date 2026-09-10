# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Keep track of where we are at in the preorder and inorder arrays
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx
            
            # If we have traversed all values in preorder, we are done with the tree
            if preIdx >= len(preorder):
                return None
            # If we have reached the value corresponding to limit, we are done
            # building this part of the tree
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            # Make new node, increment position in preorder array, and continue
            # building this part of the tree as needed
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))