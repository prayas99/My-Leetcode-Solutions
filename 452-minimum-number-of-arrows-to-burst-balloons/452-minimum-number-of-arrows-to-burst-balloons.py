class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        end = points[0][1]
        res = 1
        for i in range(1, len(points)):
            s, e = points[i]
            if s > end:
                res += 1
                end = e
            else:
                end = min(end, e)
        return res