class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(openToClose[c])
            else:
                if not stack or c != stack.pop():
                    return False
        
        return not stack
