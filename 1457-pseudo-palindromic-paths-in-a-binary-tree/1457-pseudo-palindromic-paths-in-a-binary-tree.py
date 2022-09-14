# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root = root, mask = 0):
            nonlocal ans
            if root:
                mask ^= (1 << root.val)
                if not root.left and not root.right:
                    if mask.bit_count() <= 1:
                        ans += 1
                helper(root.left, mask)
                helper(root.right, mask)
        helper()
        return ans
        