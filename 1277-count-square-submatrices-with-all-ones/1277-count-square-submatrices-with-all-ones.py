class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        
        for i in range(m):
            mat[i].append(0)
        mat.append([0 for _ in range(n + 1)])
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    mat[i][j] = min(mat[i+1][j+1], mat[i][j+1], mat[i+1][j]) + 1
                    res += mat[i][j]
        return res