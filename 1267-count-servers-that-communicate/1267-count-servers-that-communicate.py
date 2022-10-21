class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        n1 = sum(grid[i][j] for j in range(n) for i in range(m))
        rows = set()
        for i in range(m):
            if sum(grid[i]) == 1:
                rows.add(i)
        res = 0
        b = -1
        for j in range(n):
            for i in range(m):
                if grid[i][j] ==1:
                    if b == -1:
                        b = i
                    else:
                        b = -1
                        break
            if b in rows:
                res += 1
            b = -1
        return n1 - res