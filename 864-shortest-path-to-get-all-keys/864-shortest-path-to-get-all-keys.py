class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        m, n = len(grid), len(grid[0])
        
        def invalid(i, j):
            return i < 0 or j < 0 or i >= m or j >= n
        
        keys_n_locks = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].isalpha():
                    keys_n_locks += 1
                elif grid[i][j] == '@':
                    st_i, st_j = i, j
        keys = keys_n_locks//2
    
        def bfs():
            layer, q = 1, deque([(st_i, st_j, 0)])
            visited = set()
            visited.add((st_i, st_j, 0))
            while q:
                for _ in range(len(q)):
                    i, j, mask = q.popleft()
                    for dr, dc in direct:
                        i1, j1 = i + dr, j + dc
                        if invalid(i1, j1) or grid[i1][j1] == '#' or (i1, j1, mask) in visited:
                            continue
                            
                        if grid[i1][j1] == '.' or grid[i1][j1] == '@' :
                            q.append((i1, j1, mask))
                            visited.add((i1, j1, mask))
                            
                        elif grid[i1][j1].isupper():
                            idx = ord(grid[i1][j1]) - ord('A')
                            if mask & (1<<idx):
                                q.append((i1, j1, mask))
                                visited.add((i1, j1, mask))
                            
                        else:
                            idx = ord(grid[i1][j1]) - ord('a')
                            if mask | (1<<idx) == (1<<keys) - 1:
                                return layer
                            q.append((i1, j1, mask | (1<<idx)))
                            visited.add((i1, j1, mask))
                layer += 1
            return -1
        return bfs()

            
            