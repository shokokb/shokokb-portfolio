# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            s = (digits[i] + c) % 10
            c = (digits[i] + c) // 10
            digits[i] = s
            if c == 0:
                break
        if c == 1:
            digits.insert(0, c)
        return digits