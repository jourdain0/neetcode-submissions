class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(": ")", "{": "}", "[": "]"}
        q = deque()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                q.append(openToClose[c])
            else:
                if not q:
                    return False
                close = q.pop()
                if c != close:
                    return False
            
        return True if not q else False