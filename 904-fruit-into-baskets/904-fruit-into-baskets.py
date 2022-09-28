class Solution:
    def totalFruit(self, answerKey: List[int]) -> int:
        l = r = 0
        n = len(answerKey)
        d = Counter()
        res = maxi = 0
        k = 2
        while r < n:
            d[answerKey[r]] += 1
            if d[answerKey[r]] == 1:
                maxi += 1
            #window = r - l + 1
            if l <= r and maxi > k:
                d[answerKey[l]] -= 1
                if d[answerKey[l]] == 0:
                    maxi -= 1
                l += 1
                #window = r - l + 1
            res = max(res, r - l + 1)
            r += 1
        return res