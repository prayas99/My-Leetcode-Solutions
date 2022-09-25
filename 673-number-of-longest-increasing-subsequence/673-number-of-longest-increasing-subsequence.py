class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_len = res = 1
        nums[-1] = (nums[-1], 1, 1)
        for i in range(len(nums) - 2, -1, -1):
            curr_len, curr_count = 1, 1
            #print(i, nums)
            for j in range(i + 1, len(nums)):
                if nums[j][0] > nums[i]:
                    if nums[j][1] + 1 == curr_len:
                        curr_count += nums[j][2]
                    elif nums[j][1] + 1 > curr_len:
                        curr_count = nums[j][2]
                        curr_len = nums[j][1] + 1
            if curr_len > max_len:
                max_len = curr_len
                res = curr_count
            elif curr_len == max_len:
                res += curr_count
            nums[i] = (nums[i], curr_len, curr_count)
        #print(nums)
        return res
        