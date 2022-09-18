class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total // 2
        n = len(nums)
        N = n//2
        left_portion = nums[:N]
        right_portion = nums[N:]
        ans = abs(sum(left_portion) - sum(right_portion))
        
        for k in range(1, N):
            
            left_combos = [sum(comb) for comb in combinations(left_portion, k)]
            right_combos = [sum(comb) for comb in combinations(right_portion, N-k)]
            right_combos.sort()
            
            for x in left_combos:
                y = half - x
                idx = bisect.bisect_left(right_combos, y)
                if idx < len(right_combos):
                    left_sum = x + right_combos[idx]
                    ans = min(ans, abs(total - 2*left_sum))
        
        return ans
            
        