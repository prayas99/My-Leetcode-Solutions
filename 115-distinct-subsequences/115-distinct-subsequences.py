class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def helper(i = 0, j = 0):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                return helper(i + 1, j) + helper(i + 1, j + 1)
            else:
                return helper(i + 1, j)
        return helper()