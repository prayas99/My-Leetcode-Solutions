class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumi = sum([num for num in nums if num % 2 == 0])
        n, m = len(nums), len(queries)
        ans = []
        for i, (val, idx) in enumerate(queries):
            if nums[idx] % 2 == 0:
                if val % 2 == 0:
                    sumi += val
                else:
                    sumi -= nums[idx]
            else:
                if val % 2 != 0:
                    sumi += nums[idx] + val
            ans.append(sumi)
            nums[idx] += val
        return ans
        