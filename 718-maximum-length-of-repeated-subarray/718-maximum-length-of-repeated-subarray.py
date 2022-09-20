class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        prv = [0]*(n + 1)
        curr = [0]*(n + 1)
        
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = prv[j - 1] + 1
                    ans = max(ans, curr[j])
            curr, prv = [0]*(n+1), curr
        return ans