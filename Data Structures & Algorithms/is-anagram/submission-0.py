from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = defaultdict(lambda: 0)
        for c in s:
            m1[c] += 1
        for c in t:
            m1[c] -= 1
        isAn = True
        for v in m1.values():
            if v != 0:
                isAn = False
        return isAn
        