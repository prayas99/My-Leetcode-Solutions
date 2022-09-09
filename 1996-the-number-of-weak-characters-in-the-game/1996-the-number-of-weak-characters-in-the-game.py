class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j in properties:
            d[i].append(j)
        maxi = nexti = float('-inf')
        res = 0
        for k, li in sorted(d.items(), reverse = True):
            maxi = nexti
            for v in li:
                if v < maxi:
                    res += 1
                nexti = max(nexti, v)
        return res

