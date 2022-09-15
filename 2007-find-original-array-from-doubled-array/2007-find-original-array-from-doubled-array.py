class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return 
        changed.sort()
        res = Counter(changed)
        ans = []
        for i in changed:
            if res[i] == 0:
                continue
            if i % 2 == 0 and res[i//2] > 0:
                res[i] -= 1
                res[i//2] -= 1
                ans.append(i//2)
            elif res[i*2] > 0:
                res[i] -= 1
                res[i*2] -= 1
                ans.append(i)
            else:
                return
        return ans
        
        