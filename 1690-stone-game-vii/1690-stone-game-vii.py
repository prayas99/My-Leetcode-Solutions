class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def helper(i = 0, j = len(stones) - 1):
            if i >= j:
                return 0
            if j - i == 1:
                return max(stones[i], stones[j])
            opt1 = min(stones[i + 1] + helper(i + 2, j), stones[j] + helper(i + 1, j - 1))
            opt2 = min(stones[j - 1] + helper(i, j - 2), stones[i] + helper(i + 1, j - 1))
            return max(opt1, opt2)
        return helper()
        