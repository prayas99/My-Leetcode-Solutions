class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        li = sorted([dist[i] / speed[i] for i in range(n)])
        for i in range(len(li)):
            if li[i] <= i:
                return i
        return n