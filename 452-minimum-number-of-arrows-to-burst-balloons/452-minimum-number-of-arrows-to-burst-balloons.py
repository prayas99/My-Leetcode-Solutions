class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        _, end = heapq.heappop(points)
        res = 1
        while points:
            s, e = heapq.heappop(points)
            if s > end:
                res += 1
                end = e
            else:
                end = min(end, e)
        return res