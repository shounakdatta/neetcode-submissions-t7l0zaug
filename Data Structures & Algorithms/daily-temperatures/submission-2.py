from collections import deque
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        stack = deque()    # (index, num) pair

        for i, numI in enumerate(t[::-1]):
            realI = len(t)-1-i
            # print(realI, numI, stack, res)
            while stack and stack[-1][1] <= numI:
                _, index = stack.pop()
            res[realI] = stack[-1][0]-realI if stack else 0
            stack.append((realI, numI)) 
        return res