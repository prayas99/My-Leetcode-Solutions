class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n))
        rank = [1]*n
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                if rank[yy] > rank[xx]:
                    xx, yy = yy, xx
                parent[yy] = xx
                rank[xx] = max(rank[xx], rank[yy] + 1)
            else:
                return 1
                
        for i, j in edges:
            if union(i - 1, j - 1):
                return [i, j]