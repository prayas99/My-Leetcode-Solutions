class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        
        for i in range(n - 1, -1, -1):
            for j in range(2, n + 2):
                if i > j - 2:
                    continue
                option1 = nums[i] + min(dp[i+2][j], dp[i+1][j-1])
                option2 = nums[j - 2] + min(dp[i+1][j-1], dp[i][j-2])
                dp[i][j] = max(option1, option2)
                
        return dp[0][n + 1] >= sum(nums) / 2