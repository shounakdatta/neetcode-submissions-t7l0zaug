from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in groups:
                groups[ss].append(s)
            else:
                groups[ss] = [s]
        return list(groups.values())
        