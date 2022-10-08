class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target >= sum(nums[-3:]):
            return sum(nums[-3:])
        ans = sum(nums[:3])
        for i in range(len(nums)):
            if i < len(nums) - 2:
                idx = bisect_left(nums, (target - nums[i]) // 2, lo=i + 1)
                if idx == len(nums):
                    ans = nums[i] + nums[-1] + nums[-2]
                    continue
                if nums[idx] < (target - nums[i]) // 2:
                    lp, rp = idx - 1, idx
                else:
                    lp, rp = idx, idx + 1
                while lp > i and rp < len(nums):
                    if abs(target - nums[i] - nums[lp] - nums[rp]) < abs(target - ans):
                        ans = nums[i] + nums[lp] + nums[rp]
                    if nums[i] + nums[lp] + nums[rp] > target:
                        lp -= 1
                    elif nums[i] + nums[lp] + nums[rp] < target:
                        rp += 1
                    else:
                        return ans
        return ans