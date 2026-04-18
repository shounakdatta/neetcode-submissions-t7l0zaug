from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque([])
        close = {
            '}': '{', 
            ']': '[', 
            ')': '('
        }
        for c in s:
            if c in close and len(q):
                if q[-1] != close[c]:
                    return False
                q.pop()
            else:
                q.append(c)
        return len(q) == 0