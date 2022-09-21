class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for i, val in enumerate(nums):
            idx = bisect.bisect_left(ans, val)
            if idx >= len(ans):
                ans.append(val)
            else:
                ans[idx] = val
        return len(ans)
        