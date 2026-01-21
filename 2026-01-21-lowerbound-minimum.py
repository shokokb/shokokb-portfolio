class Solution:
    # Time Complexity O(log n)
    def findNumEqualOrGreaterThanTarget(self, nums:list[int], target:int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return nums[l] if  l < len(nums) else -1

def main():
    s = Solution()
    print(s.findNumEqualOrGreaterThanTarget([1,2,4,6,6,8], 0))
    print(s.findNumEqualOrGreaterThanTarget([1,2,4,6,6,8], 5))
    print(s.findNumEqualOrGreaterThanTarget([1,2,4,6,6,8], 6))
    print(s.findNumEqualOrGreaterThanTarget([1,2,4,6,6,8], 9))

main()