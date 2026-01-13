class Solution:
    # @param nums(length>=1)
    def findMin(self, nums: List[int]) -> int:
        # In the case of nums.length = 1, return nums[0] as minimum value
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[r]

        