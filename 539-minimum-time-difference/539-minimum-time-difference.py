class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, val in enumerate(timePoints):
            timePoints[i] = int(val[:2])*60 + int(val[3:])
        timePoints.sort()
        res = float('inf')
        for i in range(len(timePoints)):
            val = abs(timePoints[i] - timePoints[i - 1])
            res = min(res, val, 1440 - val)
        return res