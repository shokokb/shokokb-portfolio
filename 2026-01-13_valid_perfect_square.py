# Time Complexity : O(log n)
# Spece Complexity : O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # answer = [1, 2, ... num]
        l, r = 1, num
        while l <= r:
            m = (l+r)//2
            if m*m == num:
                return True
            elif m*m > num:
                r = m - 1
            else:
                l = m + 1
        return False
        