# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        while l <= r:   # O(n)
            if nums[l] == 0:
                zero = nums.pop(l) # O(n) 
                nums.append(zero)
                r -= 1
            else:
                l += 1