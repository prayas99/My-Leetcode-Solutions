class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def helper(i = 0, hold = -1, k = k):
            if i == n or k == 0:
                return 0
            s = prices[i]
            if s <= hold or hold == -1:
                return helper(i + 1, s, k)
            else:
                return max(helper(i + 1, hold, k), helper(i + 1, s, k - 1) + (s - hold))
        
        return helper()