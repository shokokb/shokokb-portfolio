# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(log n)
    def leftHeight(self, root: Optional[TreeNode]) -> int:
        h = 0
        n = root
        while n:
            h += 1
            n = n.left
        return h
    # O(log n)
    def rightHeight(self, root: Optional[TreeNode]) -> int:
        h = 0
        n = root
        while n:
            h += 1
            n = n.right
        return h
    # Time Complexity : O(log^2 n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        hl = self.leftHeight(root)  # O(log n)
        hr = self.rightHeight(root) # O(log n)
        if hl == hr:
            return 2 ** hl - 1      # O(1)
        else:
            # O(log n)
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        