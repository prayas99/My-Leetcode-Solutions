class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumi = sum([num for num in nums if num % 2 == 0])
        n, m = len(nums), len(queries)
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                if val % 2 == 0:
                    sumi += val
                    ans.append(sumi)
                else:
                    sumi -= nums[idx]
                    ans.append(sumi)
            else:
                if val % 2 == 0:
                    ans.append(sumi)
                else:
                    sumi += nums[idx] + val
                    ans.append(sumi)
            nums[idx] += val
        return ans
        