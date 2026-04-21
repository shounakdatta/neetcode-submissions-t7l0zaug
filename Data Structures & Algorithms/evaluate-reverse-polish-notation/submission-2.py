from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = deque([])
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y 
        }
        for c in tokens:
            if c not in ops:
                nums.append(int(c))
            else:
                y = nums.pop()
                x = nums.pop()
                nums.append(int(ops[c](x,y)))
        return int(nums[0])