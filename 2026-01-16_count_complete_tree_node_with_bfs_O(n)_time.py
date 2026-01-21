# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity : O(n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        cnt = 0
        d = deque([root])
        while d:
            n = d.popleft()
            cnt += 1
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)
        return cnt