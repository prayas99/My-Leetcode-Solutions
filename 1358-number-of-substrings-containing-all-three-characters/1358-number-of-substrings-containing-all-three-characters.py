class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        d = {'a' : 0, 'b' : 0, 'c' : 0}        
        char_left = 3
        ans = 0
        
        while j < len(s):
            if d[s[j]] == 0:
                char_left -= 1
                while i < len(s) and char_left == 0:
                    ans += (n - j)
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        char_left += 1
                    i += 1                    
            d[s[j]] += 1
            j += 1
            
        return ans
        