# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity : O(log n)
    def maxHeight(self, n: Optional[TreeNode]) -> int:
        h = 0
        while n:
            h += 1
            n = n.left
        return h

    # Time Complexity : 
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h = self.maxHeight(root)

        if h == 0:
            return 0

        cnt = 2**(h-1) - 1
        # print(h, cnt)

        n = root
        l, r = 1, 2 ** (h-1)
        while l <= r:
            m = (l+r)//2
            if n.right:
                l = m + 1
                n = n.right
            elif n.left:
                r = m
                n = n.left
            else:
                break
            print(l, r, m)
        cnt += l
        return cnt
