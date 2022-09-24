# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def helper(root = root, par = 0):
            if root:
                if par != 0:
                    graph[root.val].append((par, "U"))
                if root.left:
                    graph[root.val].append((root.left.val, "L"))
                    helper(root.left, root.val)
                if root.right:
                    graph[root.val].append((root.right.val, "R"))
                    helper(root.right, root.val)
        helper()
        def bfs():
            q = deque([(startValue, '')])
            visited = set([startValue])
            while q:
                for _ in range(len(q)):
                    curr, local = q.popleft()
                    for nexti, direct in graph[curr]:
                        if nexti in visited:
                            continue
                        if nexti == destValue:
                            return local + direct
                        q.append((nexti, local + direct))
                        visited.add(nexti)
        return bfs()