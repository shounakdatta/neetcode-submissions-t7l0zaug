from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        for n in nums:
            count[n] += 1
        pairs = list(count.items())
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_pairs[:min(len(nums), k)]]