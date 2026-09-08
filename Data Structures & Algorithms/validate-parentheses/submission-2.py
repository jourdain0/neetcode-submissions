class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = { "(" : ")", "{" : "}", "[" : "]" }
        q = deque()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                q.append(openToClose[c])
            else:
                if not q or c != q.pop():
                    return False

        return True if not q else False