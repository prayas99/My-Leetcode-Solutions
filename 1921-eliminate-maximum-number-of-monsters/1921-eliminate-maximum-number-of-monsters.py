class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        li = sorted([(dist[i]//speed[i])+1 if dist[i]%speed[i] != 0 else dist[i]//speed[i] for i in range(n)])
        res = 0
        for i in range(len(li)):
            if li[i] <= res:
                break
            res += 1
        return res