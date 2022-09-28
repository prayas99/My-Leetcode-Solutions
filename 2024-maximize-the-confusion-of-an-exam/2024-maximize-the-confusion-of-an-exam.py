class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = r = 0
        n = len(answerKey)
        d = Counter()
        res = maxi = 1
        while r < n:
            d[answerKey[r]] += 1
            maxi = max(maxi, d[answerKey[r]])
            window = r - l + 1
            while l <= r and window - maxi > k:
                d[answerKey[l]] -= 1
                l += 1
                window = r - l + 1
            res = max(res, r - l + 1)
            r += 1
        return res