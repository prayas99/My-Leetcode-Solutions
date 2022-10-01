class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = 5
        res = 0
        while a <= n:
            res += (n // a)
            a *= 5
        return res
        