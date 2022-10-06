class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        h = []
        m, n = len(matrix), len(matrix[0])
        xor = 0
        ans = []
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i - 1][j] ^ matrix[i][j - 1] ^ matrix[i - 1][j - 1]
                elif i > 0:
                    matrix[i][j] ^=  matrix[i - 1][j]
                elif j > 0:
                    matrix[i][j] ^=  matrix[i][j - 1] 
                ans.append(matrix[i][j])
        ans.sort(reverse = True)
        return ans[k - 1]