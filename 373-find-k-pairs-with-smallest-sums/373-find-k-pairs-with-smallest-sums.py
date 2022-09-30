class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(h, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        ans = []
        visi = set()
        while h and len(ans) < k:
            _, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            if (i, j + 1) not in visi:
                visi.add((i, j + 1))
                push(i, j + 1)
            if (i + 1, j) not in visi:
                visi.add((i + 1, j))
                push(i + 1, j)
        return ans