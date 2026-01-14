class Solution:
    # @summary calculate the height of Balanced Binary Tree
    # @param n node
    # @retval the height of Balanced Binary Tree
    # @retval -1 in the case the binary is inbalanced 
    # Time Complexity : O(n)
    def check(self, n: Optional[TreeNode]) -> int: 
        if not n:
            return 0
        hl = self.check(n.left)
        if hl == -1:
            return -1
        hr = self.check(n.right)
        if hr == -1:
            return -1
        if abs(hl - hr) <= 1:
            return max(hl, hr)+1
        else:
            return -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h = self.check(root) # O(n)
        return h >= 0