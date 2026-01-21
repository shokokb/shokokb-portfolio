# I find the first index where the value is greater than or equal to the target as idxL,
# and the last index where the value is less than or equal to the target as idxR.
# Then I compute the count by taking the difference.
# The time complexity is O(log n) because I use binary search.
class Solution:
    def searchTime(self, nums:list[int], target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        idxL = l

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        idxR = r
        return idxR - idxL + 1

def main():
    s = Solution()
    nums = [1,2,2,2,3,4]
    target = 2
    print("ans=", s.searchTime(nums, target))

    nums = [1,2,2,2,3,4]
    target = 0
    # idxL = 0, idxR = -1 
    print("ans=", s.searchTime(nums, target))

main()
