class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        st, end = timeSeries[0], timeSeries[0] + duration - 1
        res = duration
        for i in range(1, n):
            newend = timeSeries[i] + duration - 1
            st = timeSeries[i]
            if timeSeries[i] <= end:
                st = end + 1
            end = timeSeries[i] + duration - 1
            res += max((newend - st + 1), 0)
        return res