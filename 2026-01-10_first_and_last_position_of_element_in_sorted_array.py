class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = -1, -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        left = l

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        right = r

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]
        