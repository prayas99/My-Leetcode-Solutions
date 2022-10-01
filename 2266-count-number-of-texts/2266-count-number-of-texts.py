class Solution:
    def countTexts(self, s: str) -> int:
        n = len(s)
        def limit(c):
            if c == '7' or c=='9':
                return 3
            else:
                return 2
        @lru_cache(None)
        def helper(i = 0):
            if i >= n:
                return 1
            j = i           
            res = 0
            while j < n and j - i <= limit(s[i]) and s[j] == s[i]:
                res += helper(j + 1)
                j += 1
            return res % (int(1e9) + 7)
        return helper() % (int(1e9) + 7)
