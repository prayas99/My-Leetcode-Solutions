class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        curr, nexti = [0]*(n + 1), [0]*(n + 1)
        curr[-1] = nexti[-1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    curr[j] = nexti[j] + nexti[j + 1]
                else:
                    curr[j] =  nexti[j]
            curr, nexti = nexti, curr
            
        return nexti[0]