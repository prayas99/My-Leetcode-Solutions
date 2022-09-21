class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        n = len(word)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i, c in enumerate(word):
            if c in vowels:
                res += (n + i*(n - i - 1))
        return res