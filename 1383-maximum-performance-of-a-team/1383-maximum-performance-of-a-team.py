class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = int(1e9) + 7
        nums = sorted(zip(speed, efficiency), key = lambda x : x[1], reverse = True)
        res = float('-inf')
        h = []
        curr_sum = 0
        
        for i in range(k):
            heapq.heappush(h, nums[i])
            curr_sum += nums[i][0]
            res = max(res, curr_sum * nums[i][1])
            
        for j in range(k, n):
            sp, eff = heapq.heappop(h)
            if nums[j][0] > sp:
                heapq.heappush(h, nums[j])
                curr_sum += (nums[j][0] - sp)
                res = max(res, curr_sum * nums[j][1])
            else:
                heapq.heappush(h, (sp, eff))
                
        return res % MOD
            
        