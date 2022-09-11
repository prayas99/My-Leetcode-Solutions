class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        l, r = 1, n
        tasks.sort(reverse = True)
        
        def helper(i = 0):
                if i == n:
                    return True
                
                seti = set()
                for cont in range(mid):
                    if subset[cont] in seti:
                        continue
                    seti.add(subset[cont])
                    if subset[cont] + tasks[i] > sessionTime:
                        continue
                        
                    subset[cont] += tasks[i]
                    if helper(i + 1):
                        return True
                    subset[cont] -= tasks[i]
        
        while l <= r:
            mid = (l + r) // 2
            subset = [0] * mid       
            if helper():
                r = mid - 1
            else:
                l = mid + 1
                
        return l