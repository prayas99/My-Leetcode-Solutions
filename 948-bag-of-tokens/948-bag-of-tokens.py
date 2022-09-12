class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        i, j = 0, n - 1
        curr = res = 0
        while i <= j:
            if tokens[i] <= power:
                curr += 1
                power -= tokens[i]
                i += 1
            elif curr > 0:
                power += tokens[j]
                j -= 1
                curr -= 1
            else:
                break
            res = max(res, curr)
        return res