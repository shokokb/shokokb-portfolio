# import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # canEat Time Complexity : O(n)
        # canEat Space Complexity : O(1)
        def canEat(k:int) -> bool:
            hrs = 0
            for p in piles: # O(n)
                # hrs += math.ceil(p/k) 
                hrs += (p + k - 1) // k
                if hrs > h:
                    return False
            return hrs <= h

        # Time Complexity : O(n log max(piles))
        # Space Complexity : O(1)
        # k = [1, 2, ..., max(piles)]
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if canEat(m): # O(n)
                r = m
            else:
                l = m + 1
        return l 