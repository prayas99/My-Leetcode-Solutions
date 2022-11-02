class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        d = Counter()
        i = j = maxi = ans = 0
        while j < n:
            d[s[j]] += 1
            maxi = max(maxi, d[s[j]])
            while i <= j and (j - i + 1) - maxi > k:
                d[s[i]] -= 1
                i += 1
            ans = max(ans, (j - i + 1))
            j += 1
        return(ans)
                
            
                