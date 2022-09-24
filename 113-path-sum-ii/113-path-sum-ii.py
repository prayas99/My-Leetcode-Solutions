# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root = root, curr = 0, local = []):
            if root:
                if not root.right and not root.left:
                    if curr + root.val == targetSum:
                        res.append(local + [root.val])
                    return
                helper(root.left, curr + root.val, local + [root.val])
                helper(root.right, curr + root.val, local + [root.val])
        res = []
        helper()
        return res
        