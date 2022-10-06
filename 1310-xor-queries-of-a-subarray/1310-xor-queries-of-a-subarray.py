class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        arr.append(0)
        for idx, (i, j) in enumerate(queries):
            ans[idx] = arr[j] ^ arr[i - 1]
        return ans