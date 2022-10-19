class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        li = sorted([(dist[i]//speed[i])+1 if dist[i]%speed[i] != 0 else dist[i]//speed[i] for i in range(n)])
        #print(li)
        res = 0
        d = 0
        for i in range(len(li)):
            if li[i] <= d:
                break
            res += 1
            d += 1
        return max(1, res)