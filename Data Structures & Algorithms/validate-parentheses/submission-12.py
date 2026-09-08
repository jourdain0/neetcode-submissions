class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c in "([{":
                stack.append(openToClose[c])
            else:
                if not stack or c != stack.pop():
                    return False
        
        return not stack