# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # Get the maximum sum for the left and right side
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            
            # Update maximum value if this current path including root is greater
            res[0] = max(res[0], root.val + leftMax + rightMax)
            # Return whichever path gives you a higher sum as we go back up the tree
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]