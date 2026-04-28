import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, s) -> bool:
            hLeft = h
            for p in piles:
                hLeft -= math.ceil(p/s)
            return hLeft >= 0
        def search(left, right) -> int:
            mid = (left+right)//2
            canEatMid = canEat(piles, mid)
            if left == right:
                return mid if canEatMid else -1
            eatLeft = search(left, mid) if canEatMid else -1
            eatRight = search(min(mid+1, right), right) if not canEatMid else -1
            if eatLeft > -1:
                return eatLeft
            if canEatMid:
                return mid
            return eatRight
        return search(1, max(piles))