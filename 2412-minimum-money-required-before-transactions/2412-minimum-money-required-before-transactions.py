class Solution:
    def minimumMoney(self, tx: List[List[int]]) -> int:
        res = val = 0
        for i, j in tx:
            res += max(i - j, 0)
            val = max(val, min(i, j))
        return res + val