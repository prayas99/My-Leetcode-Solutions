class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        d = defaultdict(list)
        for i in range(n):
            (var1, var2), val = equations[i], values[i]
            d[var1].append((var2, val))
            d[var2].append((var1, 1/val))
            
        seti = defaultdict(list)
        res = [-1]*len(queries)
        for i, (v1, v2) in enumerate(queries):
            seti[(v1, v2)].append(i)
            
        def dfs(master, v, curr = 1):            
            for v2, val in d[v]:
                if (master, v2) in seti:
                    for i in seti[(master, v2)]:
                        res[i] = curr*val
                if v2 not in visited:
                    visited.add(v2)
                    dfs(master, v2, curr*val)
                    
        for v in d.keys():
            visited = set()
            dfs(v, v)
            
        return res
                
        