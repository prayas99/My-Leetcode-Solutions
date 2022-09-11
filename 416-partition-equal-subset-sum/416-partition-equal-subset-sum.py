class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2
        n = len(nums)
        
        @lru_cache(None)
        def helper(i = 0, box1 = 0, box2 = 0):
            if max(box1, box2) > total:
                return
            if i == n:
                return box1 == box2
            if box1 == box2:
                return helper(i + 1, box1 + nums[i], box2)
            return helper(i + 1, box1 + nums[i], box2) or helper(i + 1, box1, box2 + nums[i])
        
        return helper()
            