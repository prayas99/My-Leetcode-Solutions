class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = [0]*k
        n = len(nums)
        sumi = sum(nums)
        if sumi % k != 0:
            return
        val = sumi // k
        if max(nums) > val:
            return 
        nums.sort(reverse = True)
        def helper(i = 0):
            if i == n:
                return len(Counter(subsets)) == 1
            seti = set()
            for j in range(len(subsets)):                
                if subsets[j] in seti:
                    continue
                seti.add(subsets[j])
                if subsets[j] + nums[i] > val:
                    continue
                subsets[j] += nums[i]
                if helper(i + 1):
                    return True
                subsets[j] -= nums[i]
                
        return helper()