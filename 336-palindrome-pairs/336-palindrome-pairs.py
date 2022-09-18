class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def check(word):
            return word == word[::-1] # MUCH EFFICIENT THEN USING FOR LOOP
        d = {}
        for i, word in enumerate(words):
            d[word] = i
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                pref = word[:j]
                suff = word[j:]
                if check(pref):
                    back = suff[::-1]
                    if back != word and back in d:
                        res.append([d[back], i])
                if j != len(word) and check(suff):
                    front = pref[::-1]
                    if front != word and front in d:
                        res.append([i, d[front]])
        return res