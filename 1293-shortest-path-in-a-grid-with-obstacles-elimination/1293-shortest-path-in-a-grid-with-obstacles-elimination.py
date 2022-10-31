class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if m - 1 == 0 and n - 1 == 0:
            return 0
        
        def invalid(r,c):
            return r < 0 or c < 0 or r >= m or c >= n
        
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(k):
            visi, l, q = {}, 0, deque([(0, 0, k)])
            visi[(0,0)] = k
            while q:
                for _ in range(len(q)):
                    r,c,k = q.popleft()
                    for dr, dc in direc:
                        r1, c1 = r + dr, c + dc
                        if invalid(r1,c1):
                            continue
                        if (r1,c1) in visi and visi[(r1,c1)] >= k:
                            continue
                        if grid[r1][c1] == 1:
                            if k > 0:
                                q.append((r1,c1,k - 1))
                                visi[(r1,c1)] = k - 1
                            continue
                        if r1 == m - 1 and c1 == n - 1:
                            return l + 1
                        q.append((r1,c1,k))
                        visi[(r1,c1)] = k
           
                l += 1
            return -1
        return bfs(k)