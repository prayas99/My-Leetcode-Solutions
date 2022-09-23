class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                parent[yy] = xx
                
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
                    
        return n - len(Counter([find(i) for i in range(n)]))
        
        
                            
                        
                
            
        