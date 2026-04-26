class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = []
        for i, numI in enumerate(t):
            val = 0
            for j, numJ in enumerate(t[i:]):
                if numJ > numI:
                    val = j
                    break
            res.append(val)
        return res