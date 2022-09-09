class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        n -= 1
        while n:
            a, e, i, o, u = a, a + e, a + e + i, a + e + i + o, a + e + i + o + u
            n -= 1
        return a + e + i + o + u
        
        