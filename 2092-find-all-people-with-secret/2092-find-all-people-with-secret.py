class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        d = {0:0, firstPerson:0}
        ans = set()
        ans.add(0)
        ans.add(firstPerson)
        
        for x, y, t in meetings:
            adj[x].append((y, t))
            adj[y].append((x, t))
        
        
        def dfs(i , t):
            for child, time in adj[i]:
                if child in d and d[child] <= time:
                    continue
                if time < t:
                    continue
                d[child] = time
                ans.add(child)
                dfs(child, time)
               
        dfs(firstPerson, 0)
        dfs(0,0)
        return list(ans)
                