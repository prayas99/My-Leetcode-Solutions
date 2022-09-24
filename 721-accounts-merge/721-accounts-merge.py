class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [1]*n
        d = {}
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                if rank[yy] > rank[xx]:
                    xx, yy = yy, xx
                parent[yy] = xx
                rank[xx] = max(rank[xx], rank[yy] + 1)
            else:
                return 1
                
        # for i, j in edges:
        #     if union(i - 1, j - 1):
        #         return [i, j]
            
        for i in range(n):
            for j in range(1, len(accounts[i])):
                #s = accounts[i][j].split('@mail.com')[0]
                s = accounts[i][j]
                if s not in d:
                    d[s] = i
                else:
                    union(i, d[s])
        parent = [find(i) for i in range(n)]
        #print(parent, d)
        ans = [[account[0]] for account in accounts]
        for k, val in d.items():
            bisect.insort_left(ans[parent[val]], k, lo = 1)
        #print(ans)
        return [item for item in ans if len(item) > 1]