class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visi = set()
        visi.add(start)
        
        def bfs():
            layer, q = 0, deque([start])
            while q:
                for _ in range(len(q)):
                    val = q.popleft()
        
                    if val == goal:
                        return layer
                    if val < 0 or val > 1000:
                        continue
                    for n in nums:
                        if val + n not in visi:
                            q.append(val + n)
                            visi.add(val + n)
                        if val - n not in visi:
                            q.append(val - n)
                            visi.add(val - n)
                        if val ^ n not in visi:
                            q.append(val ^ n)
                            visi.add(val ^ n)
                             
                layer += 1
                
            return -1
        
        return bfs()