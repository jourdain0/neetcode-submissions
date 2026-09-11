class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        
        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # If number of opening paranthesis < n, then we can include more
            # in this branch
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()
            
            # If number of closing paranthesis < opening paranthesis, then we
            # can include one in this branch
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()
        
        dfs(0, 0)
        return res