class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        st = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        i = j = count = res = 0
        while i < n:
            if st[i] <= end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
            
        return res
        