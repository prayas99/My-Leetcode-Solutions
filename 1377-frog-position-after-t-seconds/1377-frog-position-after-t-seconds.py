class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
            
        def bfs():
            layer, q = 0, deque([(1, 1)])
            visited = set()
            visited.add(1)
            res = []
            while q and layer < t:
                for _ in range(len(q)):
                    node, curr = q.popleft()  
                    temp = 0
                    for child in d[node]:
                        if child not in visited:
                            temp += 1       
                    if temp == 0:
                        q.append((node, curr))
                    else:
                        for child in d[node]:
                            if child in visited:
                                continue
                            q.append((child, temp*curr))
                            visited.add(child)
                layer += 1
            for val, time in q:
                    if val == target:
                        res.append(time)
                        
            if not res: return 0
            ans = 1            
            for num in res:
                ans *= (1/num)
            return ans
        return bfs()
                
        
        