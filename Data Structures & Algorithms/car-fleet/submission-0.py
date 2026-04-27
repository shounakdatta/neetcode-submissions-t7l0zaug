from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        ps = sorted(pairs, key=lambda x: x[0])
        times = [(target-p)/s for p, s in ps]
        stack = deque([])
        # print(times)
        for t in times:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
