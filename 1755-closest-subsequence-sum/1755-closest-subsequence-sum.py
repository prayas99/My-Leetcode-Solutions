class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        k = n // 2
        
        sumi = sum(nums)
        
        res = min(abs(sumi - goal), abs(0 - goal))
        
        left = nums[:k]
        right = nums[k:]
        r_combo = []
        for j in range(0, len(right) + 1):
            r_combo += [sum(x) for x in combinations(right, j)]
        r_combo.sort()
        
        l_combo = []
        for i in range(0, len(left) + 1):
            l_combo += [sum(y) for y in combinations(left, i)]
            
        for val in l_combo:

            idx = bisect.bisect_left(r_combo, goal - val)
            idx = min(idx, len(r_combo) - 1)
            res = min(res, abs(goal - (val + r_combo[idx])))

            idx -= 1
            idx = max(idx, 0)
            res = min(res, abs(goal - (val + r_combo[idx])))
                
        return res