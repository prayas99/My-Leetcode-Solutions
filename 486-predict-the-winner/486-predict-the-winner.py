class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def solve(i, j):
            if i > j or i >= n or j < 0:
                return 0
            
            option1 = nums[i] + min(solve(i+2, j), solve(i+1, j-1))
            option2 = nums[j] + min(solve(i+1, j-1), solve(i, j-2))
            
            return max(option1, option2)
        
        tom = solve(0, n - 1)
        return tom >= sum(nums) / 2