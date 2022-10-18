# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def bfs():
            ans = 0
            q = deque([(root.left, 1, 0), (root.right, 1, 1)])
            while q:
                for _ in range(len(q)):
                    node, num, direct = q.popleft()
                    
                    if not node:
                        continue
                    ans = max(ans, num)
                    if node.left:
                        if direct == 1:
                            q.append((node.left, num + 1, 0))
                        else:
                            q.append((node.left, 1, 0))
                    if node.right:
                        if direct == 0:
                            q.append((node.right, num + 1, 1))
                        else:
                            q.append((node.right, 1, 1))
            return ans
        return bfs()