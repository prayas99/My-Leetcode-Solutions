class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = Counter()
        prev = {'r':'c', 'o':'r', 'a':'o', 'k':'a'}
        res = count = 0
        for c in croakOfFrogs:
            d[c] += 1
            if c == 'c':                
                count += 1
            elif c == 'k':
                if d['a'] > 0:
                    d['a'] -= 1
                    d[c] -= 1
                    count -= 1
                else:
                    return -1
            else:
                if d[prev[c]] > 0:
                    d[prev[c]] -= 1
                else:
                    return -1
            res = max(res, count)
        if any(d.values()): return -1
        return res