# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache()
        def helper(root):
            if not root:
                return 0
            
            val = 0
            
            if root.left :
                val+=helper(root.left.left) + helper(root.left.right)
                
            if root.right:
                val+= helper(root.right.left) + helper(root.right.right)
                
            return max(root.val + val, helper(root.left) + helper(root.right))
            
        return helper(root)