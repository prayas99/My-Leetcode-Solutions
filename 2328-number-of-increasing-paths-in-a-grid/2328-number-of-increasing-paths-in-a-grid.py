class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        MOD = int(1e9) + 7
        
        def invalid(i, j):
            return i < 0 or j < 0 or i >= m or j >= n
        
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        #visited = set()
        @lru_cache(None)
        def helper(i, j):
            ans = 0
            for dr, dc in direct:
                i1, j1 = i + dr, j + dc
                if invalid(i1, j1) or grid[i1][j1] <= grid[i][j]:
                    continue
                #visited.add((i1, j1))
                ans += helper(i1, j1)
            return ans + 1
        res = 0
        for i in range(m):
            for j in range(n):
                #visited = set()
                res += helper(i, j)
        return res % MOD