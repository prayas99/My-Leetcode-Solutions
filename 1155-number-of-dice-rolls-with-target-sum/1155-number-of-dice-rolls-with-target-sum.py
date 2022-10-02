class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = int(1e9) + 7
        @lru_cache(None)
        def helper(i = 0, sumi = 0):            
            if i >= n:
                if sumi == target:
                    return 1
                return 0
            ways = 0
            for j in range(1, k + 1):
                if sumi + j > target:
                    break
                ways += helper(i + 1, sumi + j)
            return ways 
        return helper() % MOD
            