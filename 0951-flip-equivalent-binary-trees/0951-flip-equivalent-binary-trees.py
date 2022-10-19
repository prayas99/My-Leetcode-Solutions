# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root, d):
            if root:
                if root.left:
                    d[root.left.val] = root.val
                    helper(root.left, d)
                if root.right:
                    d[root.right.val] = root.val
                    helper(root.right, d)
        if not root1 and not root2:
            return True
        if not root1 and root2 or root1 and not root2 or root1.val != root2.val:
            return
        d1 = {}
        helper(root1, d1)
        d2 = {}
        helper(root2, d2)
        return d1 == d2
        