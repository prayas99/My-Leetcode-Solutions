class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        nums = [0] + nums
        n = len(nums)
        mini = float('inf')
        for i, num in enumerate(nums):
                idx = bisect.bisect_left(nums, num + target, lo = i + 1)
                if idx != n:
                    mini = min(mini, idx - i)
        return mini if mini != float('inf') else 0