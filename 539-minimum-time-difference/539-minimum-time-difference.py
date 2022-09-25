class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s):
            return int(s[:2])*60 + int(s[3:])
        for i, val in enumerate(timePoints):
            timePoints[i] = convert(val)
        timePoints.sort()
        #print(timePoints)
        res = float('inf')
        for i in range(len(timePoints)):
            val = abs(timePoints[i] - timePoints[i - 1])
            res = min(res, val, 1440 - val)
        return res