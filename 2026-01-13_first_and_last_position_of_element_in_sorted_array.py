class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # Search each the left & right edge 
        # with Binary search O(log n) time

        # First position search
        # 左端探索（target以上が最初に出る位置）
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        firstPos = l

        # Last position search
        # 右端探索（target以下が最後に出る位置）
        l, r = 0, len(nums)-1
        while l <= r: 
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        lastPos = r 

        if 0 <= firstPos < len(nums) \
            and 0 <= lastPos < len(nums) \
            and firstPos <= lastPos:
            return [firstPos, lastPos]
        else:
            return [-1, -1]
                