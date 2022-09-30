class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start = points[0][0]
        end = points[0][1]
        res = 1
        for i in range(1, len(points)):
            s, e = points[i]
            if s > end:
                res += 1
                start, end = s, e
            else:
                start = max(start, s)
                end = min(end, e)
        return res