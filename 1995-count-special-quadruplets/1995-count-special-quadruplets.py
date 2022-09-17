class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        for j in range(len(nums) - 1, 2, -1):
            for a in range(0, j - 2):
                for b in range(a + 1, j - 1):
                    for c in range(b + 1, j):
                        if nums[a] + nums[b] + nums[c] == nums[j]:
                            res += 1
        return res
                    