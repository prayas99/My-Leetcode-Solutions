class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            else:
                while x != parent[x]:
                    x = parent[x]
                return x
        
        def union(x, y, flag):
            xx, yy = find(x), find(y)
            if flag == 0:
                return xx == yy
            else:
                if xx != yy:
                    parent[yy] = xx
                    
        #equations.sort(key = lambda x : x[1], reverse = True)
        
        for s in equations:
            if s[1] + s[2] == "==":
                if union(s[0], s[-1], 1):
                    return
                
        for s in equations:
            if s[1] + s[2] == "!=":
                if union(s[0], s[-1], 0):
                    return 
        return True