class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        MOD = int(1e9) + 7
        nums = sorted(zip(efficiency, speed), reverse = True)
        h = []
        curr_sum = res = 0
        
        for e, s in nums:
            heapq.heappush(h, s)
            curr_sum += s
            if len(h) > k:
                curr_sum -= heapq.heappop(h)
            res = max(res, curr_sum * e)
        
        return res % MOD
            
        