class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n):
                
                if i >= j:
                    dp[i][j] = 0
                
                elif j - i == 1:
                    dp[i][j] = max(stones[i], stones[j])
                    
                else:
                    opt1 = min(stones[i + 1] + dp[i + 2][j], stones[j] + dp[i + 1][j - 1])  
                    opt2 = min(stones[j - 1] + dp[i][j - 2], stones[i] + dp[i + 1][j - 1])
                    dp[i][j] = max(opt1, opt2)
                    
        return dp[0][n - 1]
    
#         @lru_cache(None)
#         def helper(i = 0, j = len(stones) - 1):
#             if i >= j:
#                 return 0
            
#             opt1 = min(stones[i + 1] + helper(i + 2, j), stones[j] + helper(i + 1, j - 1))
#             opt2 = min(stones[j - 1] + helper(i, j - 2), stones[i] + helper(i + 1, j - 1))
#             return max(opt1, opt2)
#         return helper()
        