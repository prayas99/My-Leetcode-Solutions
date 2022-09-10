class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @lru_cache(None)
        def helper(start = 0, m = 1):  
            if start >= n:
                return 0
            res = 0
            curr = 0
            for i in range(start, start + 2*m):
                if i >= n: break
                curr += piles[i]
                nexti = float('inf')
                for j in range(i + 1, i + 1 + 2*max(m, i + 1 - start)):
                    if j >= n:
                        break
                    nexti = min(nexti, helper(j + 1, min( max(max(m, i + 1 - start), j - i), n - j - 1)))
                res = max(res, curr + nexti if nexti != float('inf') else curr)
            return res
        
        return helper()
        