class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
            elif num > 0:
                mini = min(mini, num)
            
        if mini > 1:
            return 1
        
        for i, num in enumerate(nums):
            num = abs(num)
            if num > 0 and num - 1 < n:
                if nums[num - 1] == 0:
                    nums[num - 1] = -(n + 2)
                elif nums[num - 1] > 0:
                    nums[num - 1] *= -1
                  
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1
        return n + 1
        