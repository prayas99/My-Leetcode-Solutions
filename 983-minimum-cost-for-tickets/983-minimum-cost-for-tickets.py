class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        start, end = days[0], days[-1]
        n = len(days)
        seti = set(days)
         
        @lru_cache(None)
        def helper(i = start):
            if i > end:
                return 0
            while i not in seti:
                i += 1
            return min(helper(i + 1) + costs[0], helper(i + 7) + costs[1], helper(i + 30) + costs[2])
        
        return helper()
            