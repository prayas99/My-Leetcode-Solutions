class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        l = 1
        n = len(p) 
        res = {c : 1 for c in p}
        # print(-25//26, -25%26) # GO TO NEAREST DIVISIBLE INTEGER GREATER THAN 25 -> 26 -> QUOTIENT IS -1, REMAINDER IS -25 - (-26) = 1
        for i in range(n - 1):
            x, y = p[i], p[i + 1]
            if (ord(y) - ord(x)) % 26 == 1:
                l += 1
                res[y] = max(res[y], l)
            else:
                l = 1
        
        return sum(res.values())